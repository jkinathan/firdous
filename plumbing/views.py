from asyncio.windows_events import NULL
from django.shortcuts import render
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter
from .models import Customer,Stock,Vendor,Cheques, CashInvoice,PurchaseOrder
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
@login_required
def index(request):
    labels = []
    data = []

    if request.user.is_staff:
        customers = Customer.objects.all()
        stocks = Stock.objects.all()
        customercount = Customer.objects.all().count()
        stockscount = Stock.objects.all().count()
        vendorcount = Vendor.objects.all().count()
        context ={'customers':customers,
              'customercount':customercount,
              'stockscount':stockscount,
              'vendorcount':vendorcount
              }
    # customers = Customer.objects.filter(addedby=request.user)
    customers = Customer.objects.all()
    # print(customers)
    stocks = Stock.objects.all()
    customerCash = Customer.objects.filter(modeOfPayment='Cash')
    customerBank = Customer.objects.filter(modeOfPayment='Bank')
    customerDebtors = Customer.objects.filter(order_status='Pending').count()
    expenses = Cheques.objects.all()


    # Chart data
    for custData in customers:
        labels.append(custData.modeOfPayment)
    for custDataCash in customerCash:
        data.append(custDataCash.totalAmountPaid)
    for custDataBank in customerBank:
        data.append(custDataBank.totalAmountPaid)

    grandtotal  = 0;
    cash = 0;
    bank = 0;
    expensesTotal = 0;
    debtorBal = 0;
    accountBalance = 0;
    for Total in customers:
        grandtotal = grandtotal + Total.totalAmountPaid
    for Total in customerCash:
        cash = cash + Total.totalAmountPaid
    for Total in customerBank:
        bank = bank + Total.totalAmountPaid
    for Total in expenses:
        expensesTotal = expensesTotal + Total.totalAmountPaid
    for debtBal in customers:
        debtorBal = debtorBal + debtBal.balance
    
    for stockProfit in stocks:
        
        percstockProfit = (stockProfit.sellingPrice - stockProfit.costPrice) * 100

    print("-----------------------Blaaa_________________")
    print(percstockProfit)
    customercount = Customer.objects.all().count()
    stockscount = Stock.objects.all().count()
    vendorcount = Vendor.objects.all().count()

    accountBalance = grandtotal - expensesTotal

    context ={'customers':customers,
              'customercount':customercount,
              'stockscount':stockscount,
              'vendorcount':vendorcount,
              'grandtotal':grandtotal,
              'percstockProfit':percstockProfit,
              'cash':cash,
              'bank':bank,
              'expensesTotal':expensesTotal,
              'customerDebtors':customerDebtors,
              'debtorBal':debtorBal,
              'accoutnBalance': accountBalance,
              'labels': labels,
              'data': data,
              }
    
    for stock in stocks:
        #print(inventory)
        if request.user.is_staff and stock.piecesQuantity < 1 :
            #print(inventory)
            messages.warning(request, stock.inventoryPart+' are running low in stock Please add more!!')
            return render(request, 'index.html', context)
    
    for customer in customers:
        # if (customer.due_date )
        if customer.is_past_due and customer.due_date != NULL:
            messages.warning(request, customer.customerName+'\'s due date of '+customer.due_date.strftime("%Y-%m-%d")+ ' is past, please follow up and update!!')
            return render(request, 'index.html', context)
        
    return render(request,'index.html',context)

@login_required
def inventory(request):
    stocks = Stock.objects.all()
    for stockProfit in stocks:
        percstockProfit = (stockProfit.sellingPrice - stockProfit.costPrice) 

    context ={'stocks':stocks,
              'percstockProfit':percstockProfit
              }
    return render(request, 'inventory.html', context)

@login_required
def cash(request):
    cash = CashInvoice.objects.all()
    
    context ={'cash':cash
              }
    return render(request, 'cash.html',context)

@login_required
def purchase(request):
    purchase = PurchaseOrder.objects.all()
    
    context ={'purchase':purchase
              }
    return render(request, 'purchase.html',context)

@login_required
def check(request):
    checks = Cheques.objects.all()
    
    context ={'checks':checks
              }
    return render(request, 'check.html',context)


# @login_required
def Createcustomer(request):
    # customer = Customer()
    # inventorys = Inventory.objects.all()
    # if request.method == "POST":
    #
    #     if "createcustomer" in request.POST:
    #
    #         customer.name = request.POST["name"]
    #         customer.number = request.POST["number"]
    #
    #         inventoryid = request.POST["inventory_purchased"]
    #         customer.inventory_purchased = get_object_or_404(Inventory, id=inventoryid)
    #
    #         customer.quantity = request.POST["quantity"]
    #
    #         inventory = Inventory.objects.get(id=inventoryid)
    #
    #         if int(customer.quantity) < inventory.quantity:
    #             inventory.quantity -= int(customer.quantity)
    #             inventory.save()
    #             customer.amount = request.POST["amount"]
    #             customer.balance = inventory.price * int(customer.quantity) - int(customer.amount) * int(
    #                 customer.quantity)
    #             customer.addedby = request.user
    #             customer.save()
    #
    #             messages.success(request, 'New Customer added Successfully!!')
    #             return redirect('index')
    #
    #         else:
    #             messages.warning(request, inventory.name + ' are NOT enough in stock, please contact Administrator')
    #             return redirect('index')
    #
    # context = {'inventorys': inventorys
    #            }
    return render(request, 'customer_create.html', )


def Customerdetailfunc(request, pk):
    # inventorys = Inventory.objects.all()
    # customer = get_object_or_404(Customer, pk=pk)
    # if request.method == "POST":
    #
    #     if "editcustomer" in request.POST:
    #
    #         customer.name = request.POST["name"]
    #         customer.number = request.POST["number"]
    #
    #         inventoryid = request.POST["inventory_purchased"]
    #         customer.inventory_purchased = get_object_or_404(Inventory, id=inventoryid)
    #
    #         customer.quantity = request.POST["quantity"]
    #
    #         inventory = Inventory.objects.get(id=inventoryid)
    #         if int(customer.quantity) < inventory.quantity:
    #             inventory.quantity -= int(customer.quantity)
    #             inventory.save()
    #
    #             customer.amount = request.POST["amount"]
    #             customer.balance = inventory.price * int(customer.quantity) - int(customer.amount) * int(
    #                 customer.quantity)
    #             customer.addedby = request.user
    #             customer.save()
    #
    #             messages.warning(request, 'Customer updated Successfully!!')
    #             return redirect('index')
    #         else:
    #             messages.warning(request, 'Not enough inventory in stock, please contact Administrator')
    #             return redirect('index')

    # context = {'customer': customer, 'inventorys': inventorys}

    return render(request, 'customer_detail.html', )


# @login_required
def Createworkorder(request):
    # workorder = Workorder()
    # jobtypes = JobType.objects.all()
    # customers = Customer.objects.filter(addedby=request.user)
    # technicians = Technician.objects.all()
    # if request.method == "POST":
    #
    #     if "createworkorder" in request.POST:
    #         workorder.ordername = request.POST["ordername"]
    #         # workorder.number = request.POST["number"]
    #         customerid = request.POST["name"]
    #         workorder.customer_name = get_object_or_404(Customer, id=customerid)
    #
    #         jobid = request.POST["jobtype"]
    #         workorder.jobtype = get_object_or_404(JobType, id=jobid)
    #
    #         techid = request.POST["technician"]
    #         workorder.technician = get_object_or_404(Technician, id=techid)
    #
    #         workorder.order_status = request.POST["status"]
    #
    #         workorder.amount_paid = request.POST["amount"]
    #         workorder.balance = request.POST["balance"]
    #         workorder.save()
    #
    #         messages.success(request, 'Workorder added Successfully!!')
    #         return redirect('index')
    #
    # context = {'customers': customers, 'jobtypes': jobtypes, 'technicians': technicians
    #            }
    return render(request, 'workorder_create.html')


# @login_required
def Workorderdetailfunc(request, pk):
    # jobtypes = JobType.objects.all()
    # customers = Customer.objects.filter(addedby=request.user)
    # technicians = Technician.objects.all()
    # workorder = get_object_or_404(Workorder, pk=pk)
    # if request.method == "POST":
    #
    #     if "editworkorder" in request.POST:
    #         workorder.ordername = request.POST["ordername"]
    #         # workorder.number = request.POST["number"]
    #         customerid = request.POST["name"]
    #         workorder.customer_name = get_object_or_404(Customer, id=customerid)
    #
    #         jobid = request.POST["jobtype"]
    #         workorder.jobtype = get_object_or_404(JobType, id=jobid)
    #
    #         techid = request.POST["technician"]
    #         workorder.technician = get_object_or_404(Technician, id=techid)
    #
    #         workorder.order_status = request.POST["status"]
    #
    #         workorder.amount_paid = request.POST["amount"]
    #         workorder.balance = request.POST["balance"]
    #         workorder.save()
    #
    #         messages.success(request, 'Workorder Updated Successfully!!')
    #         return redirect('workorders')
    #
    # context = {'customers': customers, 'jobtypes': jobtypes, 'technicians': technicians, 'workorder': workorder
    #            }
    return render(request, 'workorder_detail.html')


# @login_required
def Createreturnjob(request):
    # returnjob = ReturnJobs()
    # customers = Customer.objects.filter(addedby=request.user)
    # if request.method == "POST":
    #
    #     if "createreturnjob" in request.POST:
    #         returnjob.jobname = request.POST["rjname"]
    #         # workorder.number = request.POST["number"]
    #         customerid = request.POST["name"]
    #         returnjob.customer_name = get_object_or_404(Customer, id=customerid)
    #         returnjob.complaint = request.POST["complaint"]
    #         returnjob.partnumber = request.POST["partnumber"]
    #         returnjob.datedone = request.POST["datedone"]
    #         returnjob.status = request.POST["statusr"]
    #         returnjob.save()
    #
    #         messages.success(request, 'Returnjob added Successfully!!')
    #         return redirect('returnjobs')
    #
    # context = {'customers': customers
    #           }
    return render(request, 'returnjob_create.html')


# @login_required
def Returnjobdetailfunc(request, pk):
    # customers = Customer.objects.filter(addedby=request.user)
    #
    # returnjob = get_object_or_404(ReturnJobs, pk=pk)
    # if request.method == "POST":
    #
    #     if "updatereturnjob" in request.POST:
    #         returnjob.jobname = request.POST["rjname"]
    #         # workorder.number = request.POST["number"]
    #         customerid = request.POST["name"]
    #         returnjob.customer_name = get_object_or_404(Customer, id=customerid)
    #
    #         returnjob.complaint = request.POST["complaint"]
    #         returnjob.partnumber = request.POST["partnumber"]
    #         returnjob.datedone = request.POST["datedone"]
    #         returnjob.status = request.POST["statusr"]
    #
    #         returnjob.save()
    #
    #         messages.success(request, 'Return Job Updated Successfully!!')
    #         return redirect('returnjobs')
    #
    # context = {'customers': customers, 'returnjob': returnjob
    #            }
    return render(request, 'returnjob_detail.html')

# @login_required
def workorder(request):
    # workorders = Workorder.objects.all()
    # context ={'workorders':workorders
    #          }
    return render(request, 'workorder.html', context)


# @login_required
def ReturnJobo(request):
    # returnjobs = ReturnJobs.objects.all()
    # context ={'returnjobs':returnjobs
    #           }
    return render(request, 'returnjobs.html')


# def ReportPdf(request):
#     # creating a byteStream Buffer
#     buf = io.BytesIO()
#     # create a canvas 
#     c = canvas.Canvas(buf,pagesize=letter, bottomup=0)   
#     # create a text object
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 14)


    # Adding some lines of text
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3"
    # ]

    # # Designate the model
    # customer = Customer.objects.all()

    # # Create blank list
    # lines = []

    # for customer in customer:
    #     lines.append(customer.customerName)
    #     lines.append(customer.contact)
    #     lines.append(customer.item_purchased)
    #     lines.append(customer.quantity)
    #     lines.append("-----------------")

    # # loop 
    # for line in lines:
    #     textob.textLine(line)

    # # Finish up
    # c.drawText(textob)
    # c.showPage()
    # c.save()
    # buf.seek(0)

    # # return 
    # return FileResponse(buf, as_attachment=True, filename='report.pdf')


