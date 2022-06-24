from django.urls import path, include
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('customers',views.customers,name='customers'),
     #path('dashboard/', views.dashboard, name='dashboard'),
     #path('api/data', views.get_data, name='api_data'),
     #path('api/chart/data', ChartData.as_view(), name='chart_data'),

     path('selectcurrency/',views.selectcurrency, name='selectcurrency'),
     # path('savelangcur/',views.savelangcur, name='savelangcur'),

     path('stocks/', views.inventory, name='stocks'),
     path('cash/', views.cash, name='cash'),
     path('payable/', views.payable, name='payable'),
     path('transfer/', views.transfer, name='transfer'),
     # path('receipts/', views.Receipts, name='receipts'),
     path('invoicepaymentdetail/<int:pk>',views.Receivepayment_detail, name='invoicepaymentdetail'),
     # path('paymentreceipt/', views.paymentReceipt, name='paymentreceipt'),
     path('statistics/', views.statistics, name='statistics'),
     # path('credit/', views.credit, name='credit'),
     # path('receive/', views.receive, name='receive'),
     path('purchase/', views.purchase, name='purchase'),
     path('check/', views.check, name='check'),
     path('reportstemp/', views.Reportsview, name='reportstemp'),
     # path('enterbills/', views.enterbills, name='enterbills'),
     # path('paybills/', views.paybills, name='paybills'),
     #path('technicians/', views.technician, name='technicians'),
     path('workorders/', views.workorder, name='workorders'),
     path('returnjobs/', views.ReturnJobo, name='returnjobs'),
     path('createcustomer', views.Createcustomer, name='createcustomer'),
     path('createworkorder', views.Createworkorder, name='createworkorder'),

     path('createreturnjob', views.Createreturnjob, name='createreturnjobs'),

     path('customerdetail/<int:pk>', views.Customerdetailfunc, name="customerdetail"),
     path('workorderdetail/<int:pk>', views.Workorderdetailfunc, name="workorderdetail"),

     path('returnjoborderdetail/<int:pk>', views.Returnjobdetailfunc, name="returnjobdetail"),

     # path('reportpdf', views.ReportPdf, name='reportpdf'),

]