from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
# @login_required
def inventory(request):
    # inventorys = Inventory.objects.all()
    # context ={'inventorys':inventorys
    #           }
    return render(request, 'inventory.html')


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
