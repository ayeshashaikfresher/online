from django.shortcuts import render
from app1.models import Product,CustomerModel

def customerMain(request):
    qs = Product.objects.all()
    return render(request,"customerMain.html",{"data":qs})

def customerRegistration(request):
    return render(request,"customerRegistration.html")

def saveCustomer(request):
    name = request.POST.get("full_name")
    contact = request.POST.get("contact")
    email = request.POST.get("your_email")
    pwd =request.POST.get("password")
    address = request.POST.get("address")
    status = request.POST.get("status")
    CustomerModel(name=name, contactno=contact, email=email, address=address, password=pwd,status=status).save()
    return render(request, "customerRegistration.html", {"msg": "Customer added successfully"})

def cust_Login(request):
    return render(request, "customerLogin.html")

def loginCustomer(request):
    user = request.POST.get("full_name")
    password = request.POST.get("password")
    check = CustomerModel.objects.filter(name=user,password=password)
    print(check)
    if check:
        return render(request,"welcomeCust.html",{"success":"Logged In successfully"})
    else:
        return render(request,"customerLogin.html",{"error":"Login Error"})
