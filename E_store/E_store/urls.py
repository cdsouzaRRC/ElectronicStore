from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

                path('admin/', admin.site.urls),
                path('', views.HOME, name='home'),
                path('base/', views.BASE, name='base'),
                path('account/', views.ACCOUNT, name='account'),
                path('products/', views.PRODUCTS, name='products'),
                path('search/', views.SEARCH, name='search'),
                path('products/<str:id>', views.PRODUCT_DETAIL_PAGE, name='product_detail_page'),
                path('category/', views.CATEGORY, name='category'),
                path('contact/', views.CONTACT, name='contact'),
                path('faq/', views.FAQ, name='faq'),
                path('login/', views.LOGIN, name='login'),
                path('signup/', views.SIGNUP, name='signup'),

                path('logout/', views.LOGOUT, name='logout'),
                
                path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
                path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
                path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
                path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
                path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
                path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
                path('cart/checkout/',views.CHECKOUT,name='checkout'),
                path('cart/checkout/placeorder/',views.PLACEORDER,name='placeorder'),
                path('success/',views.THANKYOU,name='thankyou'),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
