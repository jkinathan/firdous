from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=150)
    contact = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    
    def __str__(self):
        return self.name
class Stock(models.Model):

    measure = (
        ('Cartons', 'Cartons'),
        ('Pieces', 'Pieces'),
    )
    inventoryPart = models.CharField(max_length=200)
    inventoryImage = models.ImageField(null=True, blank=True,upload_to='images/')
    description = models.TextField(blank=True)
    unitMeasure = models.CharField(max_length=100, choices=measure,blank=True)
    costPrice = models.FloatField()
    sellingPrice = models.FloatField()
    percentageProfit = models.CharField(max_length=150)
    stockValue = models.CharField(max_length=150)
    quantity = models.IntegerField()
    vendorSupplied = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-name"]
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        
    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'
       
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
    customerName = models.CharField(max_length=200)
    contact = models.CharField(max_length=150, blank=True)
    item_purchased = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=False)
    rate = models.CharField(max_length=100)
    totalAmountPaid = models.FloatField()
    balance = models.FloatField()
    order_status = models.CharField(max_length=20, choices=MY_CHOICES)
    modeOfPayment = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    addedby = models.ForeignKey(User,on_delete=models.PROTECT, default=1)
    
    def get_absolute_url(self):
        return reverse("customerdetail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.customerName

class ExchangeRate(models.Model):
    currencyName = models.CharField(max_length=100)
    currencyRate = models.FloatField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.currencyName