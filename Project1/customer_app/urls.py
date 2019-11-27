from django.urls import path
from .import views

urlpatterns = [
        path('customer_main/', views.customerMain, name="customer_main"),
        path('cust_reg/', views.customerRegistration, name="cust_reg"),
        path('saveCustomer/', views.saveCustomer, name="saveCustomer"),
        path('cust_login/', views.cust_Login, name="cust_login"),
        path('loginCustomer/', views.loginCustomer, name="loginCustomer"),
]