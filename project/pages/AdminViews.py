from datetime import datetime
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import CustomUser,Staffs,Courses,Students, Subjects #using relitive path (python 3)

#_______________________________________________
# Template Load Methods
#_______________________________________________
def admin_home(request):
    #load the template as django view
    return render(request,"admin_template/home_content.html")

def add_staff(request):
    return render(request,"admin_template/add_staff_template.html")

def add_course(request):
    return render(request,"admin_template/add_course_template.html")

def add_student(request):
    courses=Courses.objects.all() #get courses for template page tag
    #calling template render and passing course list to the django tag
    return render(request,"admin_template/add_student_template.html",{"courses":courses})

def add_subject(request):
    courses=Courses.objects.all() #get course List for template page tag
    staffs=CustomUser.objects.filter(user_type=2) #filter method (used for targeting single attribute)
    #calling template render and passing course list to the django tag
    return render(request,"admin_template/add_subject_template.html",{"courses":courses,"staffs":staffs})



#_____________________________________________________
# Save/Persist Methods
#_______________________________________________________

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
            user.staffs.address=address #address not in CustomUser Table using linked table to add address
            user.save()
            messages.success(request,"User Successfully Added")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to add user. Please Ensure all fields are correct")
            return HttpResponseRedirect("/add_staff")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Post Method Not Allowed")
    else:
        course_name = request.POST.get("course_name")
        try:
            course_model=Courses(course_name=course_name)
            course_model.save()
            messages.success(request,"Course Successfully Added")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Failed to course. Please try again")
            return HttpResponseRedirect("/add_course")

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Post Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start_year = request.POST.get("start_year")
        session_end_year = request.POST.get("end_year")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=3)
            #setting attributes not in CustomUser(AbstractUser) Table
            course_obj = Courses.objects.get(id=course_id) #fetching course object to set to student
            user.students.course_id_id = course_obj
            user.students.address=address
            user.students.gender=gender
            user.students.session_start_year=session_start_year
            user.students.session_end_year=session_end_year
            user.save()
            messages.success(request,"User Successfully Added")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request,"Failed to add user. Please Ensure all fields are correct")
            return HttpResponseRedirect("/add_student")

def add_subject_save(request):
    return None