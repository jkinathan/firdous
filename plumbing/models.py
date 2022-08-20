# from asyncio.windows_events import NULL
from email.policy import default
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import datetime
from django.utils.formats import localize
import uuid
import string
import random
from currencies.models import Currency
# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=200)
    cashAccount =  models.FloatField()
    bankAccount =  models.FloatField()
    debtorBalance =  models.FloatField()
    accountBalance =  models.FloatField()
    expensesTotal =  models.FloatField()
    grandTotal =  models.FloatField()
    cashFromReceipts =  models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    contact = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    
    def __str__(self):
        return self.name
class Stock(models.Model):

    # measure = (
    #     ('Cartons', 'Cartons'),
    #     ('Pieces', 'Pieces'),
    # )
    inventoryPart = models.CharField(max_length=200)
    inventoryImage = models.ImageField(null=True, blank=True,upload_to='images/')
    description = models.TextField(blank=True)
    # unitMeasure = models.CharField(max_length=100, choices=measure,blank=True)
    # cartonQuantity = models.IntegerField(default=1, blank=True)
    piecesQuantity = models.IntegerField(default=1, blank=True)
    costPrice = models.FloatField()
    sellingPrice = models.FloatField()
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    percentageProfit = models.CharField(max_length=150, blank=True)
    # quantity = models.IntegerField()
    vendorSupplied = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Calcuting percentageprofit
    def calculate_percentageProfit(self):
        #self.aggregate(sum=Sum('installment_amount'))
        percentageProfit = ((self.sellingPrice - self.costPrice) / self.costPrice) * 100
        return percentageProfit

    class Meta:
        ordering = ["-inventoryPart"]
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        
    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.inventoryImage.url))
    picture_tag.short_description = 'Picture'
       
    # Saving percentageProfit
    def save(self,*args, **kwargs):
        self.percentageProfit = self.calculate_percentageProfit()
        super().save(*args, **kwargs)
    # def serialize(self):
    #     return self.__dict__
    def __str__(self):
        return self.inventoryPart


class Customer(models.Model):
    MY_CHOICES = (
        ('Complete', 'Complete'),
        ('Pending', 'Pending'),
        ('Incomplete', 'Incomplete'),
    )
    shopOptions = (
        ('firdous', 'firdous'),
        ('sj', 'sj'),
    )
    paymentMode = (
        ('Bank', 'Bank'),
        ('Cash', 'Cash'),
    )
    customerName = models.CharField(max_length=200)
    contact = models.CharField(max_length=150, blank=True)
    item_purchased = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=False)
    totalAmountPaid = models.FloatField(default=0.00)
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.FloatField(default=0.00)
    order_status = models.CharField(max_length=20, choices=MY_CHOICES)
    modeOfPayment = models.CharField(max_length=100, choices=paymentMode)
    purchased_From = models.CharField(default='sj', max_length=20, choices=shopOptions)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"),blank=True,null=True)
    addedby = models.ForeignKey(User,on_delete=models.PROTECT, default=1)

    # Calcuting balance
    def calculate_balance(self):
        balance = (self.item_purchased.sellingPrice*self.quantity - self.totalAmountPaid) 
        return balance
               
    # Updating Order Status
    def update_Order_status(self):
        if(self.balance < 0.5):
            order_status = 'Complete'
        else:
            order_status = 'Pending'
        return order_status
    
    # Updating Due date
    def update_Due_Date(self):
        if(self.balance < 0.5):
            self.due_date = None
        return self.due_date
    
    def get_absolute_url(self):
        return reverse("customerdetail", kwargs={"pk": self.pk})

    @property
    def is_past_due(self):
        if self.due_date:
            # formatted_datetime = formats.date_format(date.today(), "%Y-%m-%d")
            return datetime.now().strftime("%Y-%m-%d") > self.due_date.strftime("%Y-%m-%d")

    # Saving Changes
    def save(self,*args, **kwargs):
        self.balance = self.calculate_balance()
        self.order_status = self.update_Order_status()
        self.update_Due_Date = self.update_Due_Date()

        self.item_purchased.piecesQuantity -= self.quantity
        self.item_purchased.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.customerName

class ExchangeRate(models.Model):
    currencyName = models.CharField(max_length=100)
    currencyRate = models.FloatField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.currencyName

class CashInvoice(models.Model):

    paymentMode = (
        ('Bank', 'Bank'),
        ('Cash', 'Cash'),
    )

    customerName = models.ForeignKey(Customer, on_delete=models.CASCADE)
    receiptNumber = models.CharField(max_length=150)
    modeOfPayment = models.CharField(max_length=100, choices=paymentMode, default='Cash')
    item_purchased = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=False)
    totalAmountPaid = models.FloatField()
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.FloatField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))


    # Calcuting balance
    def calculate_balance(self):
        balance = (self.item_purchased.sellingPrice*self.quantity - self.totalAmountPaid) 
        return balance
    
    # Saving changes
    def save(self,*args, **kwargs):
        self.balance = self.calculate_balance()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.customerName)

class PurchaseOrder(models.Model):
    vendorName = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_purchased = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=False)
    totalAmountPaid = models.FloatField()
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.FloatField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))


    # Calcuting balance
    def calculate_balance(self):
        balance = (self.item_purchased.sellingPrice*self.quantity - self.totalAmountPaid) 
        return balance
    
    # Saving changes
    def save(self,*args, **kwargs):
        self.balance = self.calculate_balance()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.vendorName)

class Cheques(models.Model):

    shopOptions = (
        ('firdous', 'firdous'),
        ('sj', 'sj'),
    )

    # chequeId = random.randint(1, 900000000)
    chooseAccount = models.CharField(default='sj', max_length=20, choices=shopOptions)
    expenseName = models.CharField(max_length=150)
    expenseCost = models.FloatField()
    expenseQuantity = models.IntegerField(default=1,null=False)
    totalAmountPaid = models.FloatField()
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.FloatField(default=0.0)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        ordering = ["-expenseName"]
        verbose_name = 'Cheque'
        verbose_name_plural = 'Cheques' 
        
    # Calcuting balance
    def calculate_balance(self):
        balance = (self.expenseCost*self.expenseQuantity - self.totalAmountPaid) 
        return balance

    def save(self,*args, **kwargs):
        self.balance = self.calculate_balance()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'C-'+str(self.pk)


class Payable(models.Model):
    
    vendorSupplied = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item_supplied = models.ForeignKey(Stock, on_delete=models.CASCADE)
    amountToPay = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return str(self.vendorSupplied)

class Transfer(models.Model):
    paymentMode = (
        ('Bank', 'Bank'),
        ('Cash', 'Cash'),
    )
    account = (
        ('firdous', 'firdous'),
        ('sj', 'sj'),
    )
    MY_CHOICES = (
            ('Complete', 'Complete'),
            ('Pending', 'Pending'),
            ('Incomplete', 'Incomplete'),
        )
    # InvoiceNumber = random.randint(1, 900000000)
    vendor = models.ForeignKey(Payable, on_delete=models.CASCADE)
    modeOfPayment = models.CharField(max_length=100, choices=paymentMode,default='Cash')
    amountPaid = models.FloatField(default=0.00)
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    chooseAccount = models.CharField(max_length=200, choices=account,default='sj')
    Balance = models.FloatField(default=0.00)
    status = models.CharField(max_length=20, choices=MY_CHOICES,default='Pending')
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    # Calcuting balance
    def calculate_balance(self):
        Balance = (self.vendor.amountToPay - self.amountPaid) 
        return Balance

    # Updating Order Status
    def update_status(self):
        if(self.Balance < 0.5):
            status = 'Complete'
        else:
            status = 'Pending'
        return status

    # Saving changes
    def save(self,*args, **kwargs):
        self.Balance = self.calculate_balance()
        self.status = self.update_status()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.vendor)


# Receipt model
class CustomerReceipt(models.Model):

    receiptNumber = models.CharField(max_length=150)
    customerName = models.CharField(max_length=150)
    modeOfPayment = models.CharField(max_length=100,default='Cash')
    item_purchased = models.CharField(max_length=250)
    purchasedFrom = models.CharField(max_length=150, blank=True,default=0)
    quantity =  models.CharField(max_length=150, blank=True,default=0)
    price = models.CharField(max_length=150, blank=True,default=0)
    discount =  models.CharField(max_length=150, blank=True,default=0)
    totalAmountPaid =  models.CharField(max_length=150, blank=True,default=0)
    # AmountAfterDiscount = models.FloatField()
    balance = models.CharField(max_length=150, blank=True,default=0)

    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))


    # # Calcuting discount
    # def calculate_discount(self):
    #     mydiscount = ((self.discount/100)*(self.item_purchased.sellingPrice*float(self.quantity)))
    #     AmountAfterDiscount = ((self.item_purchased.sellingPrice*float(self.quantity)) - mydiscount)
    #     return AmountAfterDiscount
    
    # Saving changes
    def save(self,*args, **kwargs):
        # self.AmountAfterDiscount = self.calculate_discount()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.receiptNumber)