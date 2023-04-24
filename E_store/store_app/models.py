
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
alphaSpaces = RegexValidator(r'^[a-zA-Z]+$', 'Only letters are allowed')
numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class Categories(models.Model):
    name = models.CharField(max_length=200, validators=[alphaSpaces])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Catergories'


class Brand(models.Model):
    name = models.CharField(max_length=200,  validators=[alphaSpaces])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Brand'


class Color(models.Model):
    name = models.CharField(max_length=200,  validators=[alphaSpaces])
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Color'


class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('100 TO 1000', '100 TO 1000'),
        ('1000 TO 10000', '1000 TO 10000'),
        ('10000 TO 20000', '10000 TO 20000'),
        ('20000 TO 30000', '20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO ABOVE', '40000 TO ABOVE'),

    )
    price = models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price
    
    class Meta:
        verbose_name_plural = 'Filter_Price'


    
    

class Product(models.Model):
    CONDITION = (('Product', 'Product'), ('New Product', 'New Product'), ('Top Rated', 'Top Rated'),
                 ('Featured Product', 'Featured Product'),)
    STOCK = (('In Stock', 'In Stock'), ('Out Of Stock', 'Out Of Stock'))
    STATUS = (('Publish', 'Publish'), ('Draft', 'Draft'))

    unique_id = models.CharField(unique=True, max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='Product_images/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = RichTextField()
    description = RichTextField()
    tag = RichTextField()
    status = models.CharField(choices=STATUS, max_length=200)


    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_created=True, null=True)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Product'


class Images(models.Model):
    image = models.ImageField(upload_to='Product_images/img')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Images'


class Contact_Us(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Contact Us'

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=200)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = 'Faq'

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_images/img')
    price = models.IntegerField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Slider'


class Review(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    rating = models.IntegerField()
    product_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Review'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)
    town_city =models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode =models.IntegerField()
    phone = models.CharField(max_length=50)
    email =models.EmailField(max_length=50)
    addition = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=200, null=True, blank=True)
    paid = models.BooleanField(default= False, null= True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Order'
    
STATUS = (
    ('Pending','PENDING'),
    ('Packed', 'PACKED'),
    ('Shipping','SHIPPING'),
    ('Delivered','DELIVERED'),
)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_images/img')
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    total = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default='Pending', null=True)
    
    
    
    def __str__(self):
            return self.order.user.username
        
    class Meta:
        verbose_name_plural = 'Order Items'
        
numeric = RegexValidator(r'^[6-9]\d{9}$', 'Enter Valid Phone Number')
pin =  RegexValidator(r'\d{6}', 'Enter Valid Pincode')
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, validators=[alphaSpaces])
    town_city =models.CharField(max_length=50, validators=[alphaSpaces])
    state = models.CharField(max_length=50, validators=[alphaSpaces])
    postcode =models.CharField(max_length=6, validators=[pin])
    phone = models.CharField(max_length=10, validators=[numeric])
    
    def __str__(self):
            return self.user.username
        
    class Meta:
        verbose_name_plural = 'Address'