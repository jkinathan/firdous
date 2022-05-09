from django.contrib import admin
from .models import *

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ['inventoryPart','picture_tag','cartonQuantity', 'costPrice','piecesQuantity','vendorSupplied']
    readonly_fields = ['percentageProfit']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customerName','item_purchased','quantity', 'order_status', 'due_date']
    readonly_fields = ['balance','order_status']

admin.site.register(Vendor),
admin.site.register(Stock,StockAdmin),
admin.site.register(Customer, CustomerAdmin),
admin.site.register(ExchangeRate),