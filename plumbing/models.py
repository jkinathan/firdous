from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import datetime
from django.utils.formats import localize
# Create your models here.


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
    cartonQuantity = models.IntegerField(default=1, blank=True)
    piecesQuantity = models.IntegerField(default=1, blank=True)
    costPrice = models.FloatField()
    sellingPrice = models.FloatField()
    percentageProfit = models.CharField(max_length=150, blank=True)
    stockValue = models.CharField(max_length=150)
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
    totalAmountPaid = models.FloatField()
    balance = models.FloatField()
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

    # Saving percentageProfit
    def save(self,*args, **kwargs):
        self.balance = self.calculate_balance()
        self.order_status = self.update_Order_status()
        self.update_Due_Date = self.update_Due_Date()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.customerName

class ExchangeRate(models.Model):
    currencyName = models.CharField(max_length=100)
    currencyRate = models.FloatField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.currencyName