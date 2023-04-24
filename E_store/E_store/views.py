
from email.charset import add_charset
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from store_app.models import Product, Categories, Filter_Price, Color, Brand, Contact_Us, Slider, Review, Faq, Order, OrderItem, Address
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db.models import Avg
from django.db.models.functions import Cast
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ProfileForm, EditAddForm

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET ))


def BASE(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    
    

    context = {
        'product': product,
        'categories': categories,
        
    }
    return render(request, 'Main/base.html', context)


def HOME(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    slider = Slider.objects.all()
   

    context = {
        'product': product,
        'categories': categories,
        'slider': slider,
    }
    return render(request, 'Main/index.html', context)


def PRODUCTS(request):
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICE_LTOHID = request.GET.get('PRICE_LTOH')
    PRICE_HTOLID = request.GET.get('PRICE_HTOL')

    if CATID:
        product = Product.objects.filter(categories=CATID, status='Publish')
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(filter_price=PRICE_FILTER_ID, status='Publish')
    elif COLORID:
        product = Product.objects.filter(color=COLORID, status='Publish')
    elif BRANDID:
        product = Product.objects.filter(brand=BRANDID, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif PRICE_LTOHID:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif PRICE_HTOLID:
        product = Product.objects.filter(status='Publish').order_by('-price')
    else:
        product = Product.objects.filter(status='Publish')

    paginator = Paginator(product, 6)
    page = request.GET.get("page", 1)

    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(1)
    


    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand,

    }
    return render(request, 'Main/products.html', context)


def SEARCH(request):
    query = request.GET.get('query')
    categories = Categories.objects.all()
    product = Product.objects.filter(tag__icontains=query)

    context = {
        'product': product,
        'categories': categories,

    }
    return render(request, 'Main/search.html', context)


def PRODUCT_DETAIL_PAGE(request, id):
    prod = Product.objects.filter(id=id).first()
    categories = Categories.objects.all()
    reviews = Review.objects.filter(product_id=id)
    count = Review.objects.filter(product_id=id).count()
    averages = Review.objects.filter(product_id=id).aggregate(Avg('rating'))
    average = averages['rating__avg']
   

    if request.method == 'POST':
        Name = request.POST.get('name')
        message = request.POST.get('message')
        ratings = request.POST.get('rating')
        product_id = id
        review = Review(
            name=Name,
            message=message,
            rating=ratings,
            product_id = product_id,

        )
        review.save()
        return redirect('product_detail_page', id)
   
    
   

    context = {
        'prod': prod,
        'categories': categories,
        'review': reviews,
        'count': count,
        'average': average,
        
        
    }
    return render(request, 'Main/productsingle.html', context)


def CATEGORY(request):
    categories = Categories.objects.all()
    product = Product.objects.filter(status='Publish')

    CATID = request.GET.get('categories')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICE_LTOHID = request.GET.get('PRICE_LTOH')
    PRICE_HTOLID = request.GET.get('PRICE_HTOL')

    if ATOZID:
        product = Product.objects.filter(categories=CATID, status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(categories=CATID, status='Publish').order_by('-name')
    elif PRICE_LTOHID:
        product = Product.objects.filter(categories=CATID, status='Publish').order_by('price')
    elif PRICE_HTOLID:
        product = Product.objects.filter(categories=CATID, status='Publish').order_by('-price')
    else:
        product = Product.objects.filter(categories=CATID, status='Publish')

    context = {

        'categories': categories,
        'product': product,
    }

    return render(request, 'Main/category.html', context)



@login_required(login_url="/login/")
def CONTACT(request):
    categories = Categories.objects.all()
    product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
        'categories': categories,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact_Us(
            name=name,
            subject=subject,
            message=message,

        )
        contact.save()
        messages.success(request, "Your Message is been Received")
        return redirect('home')

    return render(request, 'Main/contact.html', context)

def FAQ(request):
    categories = Categories.objects.all()
    faq = Faq.objects.all()

    context = {
        'faq': faq,
        'categories': categories,
    }
    return render(request, 'Main/faq.html', context)

def LOGIN(request):
    categories = Categories.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect('home')
            
        else:
            messages.error(request, ("Incorrect Username or Password"))
            return redirect('login')


    context = {
        'categories': categories,
     }

    return render(request, 'Main/login.html',context)


def SIGNUP(request):
    categories = Categories.objects.all()
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(pass1) < 8:
            messages.error(request, "Minimum 8 characters")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords Does Not Match")
            return redirect('signup')
        
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists! Try logging in.')
            return redirect('signup')
        else:

            customer = User.objects.create_user(username, email, pass1)
            customer.first_name = fname
            customer.last_name = lname
            
            customer.save()
            messages.success(request, "Registered Successfully")
            return redirect('login')

    context = {
        'categories': categories,
     }

    return render(request, 'Main/signup.html',context)





def LOGOUT(request):
    logout(request)
    return render(request, 'Main/login.html')



@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, "Added to Cart")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    messages.info(request, "Item has been Removed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.info(request, "Cart is Empty")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/login/")
def cart_detail(request):
    categories = Categories.objects.all()
    
    context = {
        'categories': categories,
    }
    return render(request, 'cart/cart_detail.html', context)

@login_required(login_url="/login/")
def CHECKOUT(request):
    
    categories = Categories.objects.all()
    amnt = request.POST.get('amount')
    amt = float(amnt)
    amount = int(amt)*100+10000
    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
        })

    order_id = payment['id']
    
    userprofile = Address.objects.filter(user=request.user.id).first()
    context = {
        'order_id' : order_id,
        'payment' : payment,
        'categories': categories,
        'userprofile': userprofile,
    }
    return render(request, 'cart/checkout.html', context)


@login_required(login_url="/login/")
def PLACEORDER(request):
    if request.method == "POST":
        
        currentuser = User.objects.filter(id=request.user.id).first()
        
        if not currentuser.first_name :
            currentuser.first_name = request.POST.get('firstname')
            currentuser.last_name = request.POST.get('lastname')
            currentuser.save()
            
        
        if not Address.objects.filter(user=request.user):
            userprofile = Address()
            userprofile.user = request.user 
            userprofile.address = request.POST.get('address')
            userprofile.town_city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.postcode = request.POST.get('postcode')
            userprofile.phone = request.POST.get('phone')  
            userprofile.save()     
         
        userid = request.session.get('_auth_user_id')
        user = User.objects.get(id=userid)
        cart = request.session.get('cart')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        address = request.POST.get('address')
        town_city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        addition = request.POST.get('message')
        payment = request.POST.get('payment')
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        categories = Categories.objects.all()
        
        
        context ={
            
        }

        order = Order(
            user = user,
            first_name = first_name,
            last_name = last_name,
            address = address,
            town_city = town_city,
            state = state,
            postcode = postcode,
            phone = phone,
            email = email,
            addition = addition,
            payment_id = order_id,
            amount=amount,


        )
        order.save()
        for i in cart:
            a = (int(cart[i]['price']))
            b = (cart[i]['quantity'])
            total = a * b

            item = OrderItem(
                user = user,
                order = order,
                product = cart[i]['name'],
                image = cart[i]['image'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total = total


            )
            item.save()
            
    
        mail = Order.objects.last()   
        categories = Categories.objects.all()
            
        context = {
            'mail' : mail,
            'categories': categories,
            'order_id' : order_id,
            
            'categories': categories,
        }
            

        return render(request, 'cart/placeorder.html', context)

@csrf_exempt
def THANKYOU(request):
    
    categories = Categories.objects.all()
    if request.method == "post":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
            
        user = Order.objects.filter(payment_id = order_id).first()
        user.paid = True 
        user.save()
    
    cart = Cart(request)
    cart.clear()  
        
    context = {
        'categories': categories,
    }
    return render(request, 'cart/thankyou.html', context)

@login_required(login_url="/login/")
def ACCOUNT(request):
    categories = Categories.objects.all()
    userid = request.session.get('_auth_user_id')
    user = User.objects.get(id=userid)
    order= reversed(OrderItem.objects.filter(user = user))
    add = Address.objects.filter(user=request.user.id).first()
    ordercount = OrderItem.objects.filter(user = user).count()
    Pform = ProfileForm(instance = request.user )   
       
    if request.method ==  "POST":
        pfm = ProfileForm(request.POST, instance=request.user)
        if pfm.is_valid():
            pfm.save()
            messages.success(request, "Updated Profile Successfully")
            return redirect('account')
    else:
        pfm = ProfileForm(instance=request.user) 
    
    if request.method == 'POST': 
        form = EditAddForm(request.POST,instance=add)   
        if form.is_valid():
            saveform = form.save(commit=False)
            saveform.user = request.user
            saveform.save() 
            messages.success(request, "Address Updated Successfully")
            return redirect('account')
        else:
            messages.error(request, "Address Updated Unsuccessful")
    else:
        form = EditAddForm(instance=add)  
        
           
    
    return render(request, 'Main/account.html', {
        'order' : order,
        'categories': categories,
        'address': add,
        'Pform': Pform,
        'form':form,
        'ordercount': ordercount,
        })
    
def ABOUTUS(request):
    return render(request, 'Main/aboutus.html')