from django.shortcuts import render


def admin_home(request):
    #load the template as django view
    return render(request,"admin_template/home_content.html")

def add_staff(request):
    return render(request,"admin_template/add_staff_template.html")