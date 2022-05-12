from django.urls import path, include
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     #path('dashboard/', views.dashboard, name='dashboard'),
     #path('api/data', views.get_data, name='api_data'),
     #path('api/chart/data', ChartData.as_view(), name='chart_data'),

     path('stocks/', views.inventory, name='stocks'),
     path('cash/', views.cash, name='cash'),
     # path('credit/', views.credit, name='credit'),
     # path('receive/', views.receive, name='receive'),
     path('purchase/', views.purchase, name='purchase'),
     path('check/', views.check, name='check'),
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