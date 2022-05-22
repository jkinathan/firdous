from django.contrib import admin
from .models import *

# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ['inventoryPart','picture_tag','cartonQuantity', 'costPrice','piecesQuantity','vendorSupplied']
    readonly_fields = ['percentageProfit']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customerName','item_purchased','quantity', 'order_status', 'due_date']
    readonly_fields = ['balance','order_status']
    
class PurchaseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ['balance']

class CashInvoiceAdmin(admin.ModelAdmin):
    readonly_fields = ['balance']

class ChequesAdmin(admin.ModelAdmin):
    readonly_fields = ['chequeId','balance']

class TransferAdmin(admin.ModelAdmin):
    readonly_fields = ['InvoiceNumber','Balance','status']

admin.site.register(Vendor),
admin.site.register(Stock,StockAdmin),
admin.site.register(Customer, CustomerAdmin),
admin.site.register(ExchangeRate),
admin.site.register(CashInvoice, CashInvoiceAdmin),
admin.site.register(PurchaseOrder, PurchaseOrderAdmin),
admin.site.register(Cheques,ChequesAdmin),
admin.site.register(Payable),
admin.site.register(Transfer,TransferAdmin),



