from django.contrib import admin

# Register your models here.
from .models import *


class ImagesTublerinline(admin.TabularInline):
    model = Images


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline]
    
    list_display = ("name", "price", "condition","categories","brand")
    
class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem

class OrderItemAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerinline]
    list_display = ("user","date", "amount", "payment_id", "paid")   
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "town_city", "state", "postcode")
    
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")
    
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "status")   

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "rating")   
    
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Contact_Us, ContactUSAdmin)
admin.site.register(Faq)
admin.site.register(Slider)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderItemAdmin)
admin.site.register(OrderItem, OrdersAdmin)
admin.site.register(Address, AddressAdmin)