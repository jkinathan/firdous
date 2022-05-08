from django.contrib import admin
from .models import *

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ['inventoryPart','picture_tag','cartonQuantity', 'costPrice','piecesQuantity','vendorSupplied']
    readonly_fields = ['percentageProfit']

admin.site.register(Vendor),
admin.site.register(Stock,StockAdmin),
admin.site.register(Customer),
admin.site.register(ExchangeRate),