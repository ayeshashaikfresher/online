from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from .models import MerchantModel,Product,CustomerModel
import random
import requests

def loginPage(request):
      return render(request,"loginpage.html")

def checkUser(request):
    user = request.POST.get("uname")
    password = request.POST.get("psw")
    if user=="admin" and password=="admin":
        return render(request, "welcomePage.html", {"success": "Welcome  " + user})
    else:
        return render(request, "loginpage.html", {"error": "Check ur details"})

def addMerchant(request):
    return render(request,"addMerchant.html")

def generate():
    id = MerchantModel.objects.values_list("idno")
    l = len(id)
    if (l != 0):
        return id[l - 1][0] + 1
    else:
        return 101

def saveMerchant(request):
    idno = generate()
    name = request.POST.get("username")
    contact = request.POST.get("contact")
    email = request.POST.get("email")
    pwd = random.randint(10000, 50000)
    MerchantModel(idno=idno, name=name, contact=contact, email=email, password=pwd).save()
    M1 = MerchantModel.objects.all()
    return render(request, "addMerchant.html", {"msg": "merchant add successfully", "data": M1})

def viewMerchant(request):
    merchant = MerchantModel.objects.all()
    return render(request, 'viewMerchant.html', {"data": merchant})

def deleteMerchant(request):
    id = request.GET.get("idno")
    MerchantModel.objects.filter(idno=id).delete()
    mm = MerchantModel.objects.all()
    return render(request, "viewMerchant.html", {"data": mm,"delete":"Merchant Deleted Successfully"})

def logOut(request):
    return render(request, "loginpage.html", {"logout": "Logout Succesfully"})

@method_decorator(csrf_exempt,name="dispatch")
class Writeone(View):
    def post(self, request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        email = ''
        password = ''
        for x in jd:
            # print(x,jd[x])
            if x == 'email':
                email = jd[x]
            else:
                password = jd[x]
        d = MerchantModel.objects.filter(email=email,password=password)
        print(d)
        if d:
            js = json.dumps({"msg": "valid Details"})
            return HttpResponse(js,content_type="application/json")
            #return HttpResponse(json.dumps({}), content_type="application/json")
        else:
            js = json.dumps({"msg": "Invalid Details"})
            return HttpResponse(js,content_type="application/json")
        # p = Product(jd)
        # p.save()


@method_decorator(csrf_exempt,name='dispatch')
class Addproduct(View):
    def post(self,request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        no = jd["pro_no"]
        name = jd["name"]
        price = jd["price"]
        quantity = jd["quantity"]
        print(jd["pro_no"])
        ef = Product(pro_no=no, name=name, price=price, quantity=quantity).save()
        js = json.dumps({"msg": "product is saved"})
        return HttpResponse(js, content_type="application/json")

@method_decorator(csrf_exempt,name='dispatch')
class Changepwd(View):
    def post(self,request):
        data = request.body
        print(data)
        jd = json.loads(data)
        print(jd)
        email=jd['email']
        old=jd['old']
        new=jd['new']
        confirm=jd['confirm']
        if new==confirm:
            p=MerchantModel.objects.filter(email=email,password=old).update(password=confirm)
            print(p)
        else:
            js = json.dumps({"msg": "False"})
            return HttpResponse(js, content_type="application/json")
        if p:
            js = json.dumps({"msg": "password changed"})
            return HttpResponse(js, content_type="application/json")
        else:
            js = json.dumps({"msg": "0"})
from django.core.serializers import serialize
class Readone(View):
    def get(self,request):
        qs=MerchantModel.objects.all()
        json_data=serialize("json",qs,fields=('email','password'))
        return HttpResponse(json_data,content_type="application/json")

class ReadAllProducts(View):
    def get(self, request):
        qs = Product.objects.all()
        json_data = serialize("json",qs)
        return HttpResponse(json_data,content_type="application/json")

def deletePro(self,request,pro_no):
    try:
        old_data = Product.objects.filter(pro_no=pro_no).delete()
        print(old_data)
    except Product.DoesNotExist:
        json_mess = json.dumps({"error_message": "Given IDNO is Invalid"})
        return HttpResponse(json_mess, content_type="application/json")
    else:
        json_mess = json.dumps({"message": "Product  is Deleted"})
        return HttpResponse(json_mess, content_type="application/json")
