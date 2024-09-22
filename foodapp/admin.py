# foodapp/admin.py
from django.contrib import admin
from .models import Product
from .models import Contact

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'category', 'sub_category', 'price', 'pub_date', 'image')
    search_fields = ('product_name', 'category', 'sub_category', 'price', 'desc')
    list_filter = ('category', 'sub_category', 'pub_date')
    ordering = ('-pub_date',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'Name', 'Email_Address', 'Subject', 'Message')
    search_fields = ('Name', 'Email_Address', 'Subject', 'Message')
    ordering = ('-customer_id',)
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)    
admin.site.register(Product, ProductAdmin)
