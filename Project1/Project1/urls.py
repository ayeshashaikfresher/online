"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.loginPage, name="main"),
    path('checklogin/', views.checkUser, name="checklogin"),
    path('addmerchant/', views.addMerchant, name="addmerchant"),
    path('saveMerchant/', views.saveMerchant, name="saveMerchant"),
    path('viewmerchant',views.viewMerchant,name="viewmerchant"),
    path('deletemerchant',views.deleteMerchant,name="deletemerchant"),
    path('logout/', views.logOut, name="logout"),

    path('writeone/',views.Writeone.as_view(),name="writeone"),
    path('readone/',views.Readone.as_view(),name="readone"),
    path('addproduct/',views.Addproduct.as_view(),name="addproduct"),
    path('changepwd/',views.Changepwd.as_view(),name="changepwd"),

     path('all/',views.ReadAllProducts.as_view(),name="all"),
     path('delete/<int:pro_id>',views.deletePro,name="delete"),

     path('',include('customer_app.urls'),name="customerapp"),

]
