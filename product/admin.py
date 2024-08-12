from django.contrib import admin

from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Monitoring from admin panel.
    """
    
    list_display = ["user", "title"]
