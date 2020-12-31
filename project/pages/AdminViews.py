from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import CustomUser,Staffs #using relitive path (python 3)


def admin_home(request):
    #load the template as django view
    return render(request,"admin_template/home_content.html")

def add_staff(request):
    return render(request,"admin_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Post Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.staffs.address=address #address not in CustomUser Table using linked table for address
            user.save
            messages.success(request,"User Successfully Added")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to add user. Please Ensure all fields are correct")
            return HttpResponseRedirect("/add_staff")