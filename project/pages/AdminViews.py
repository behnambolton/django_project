from datetime import datetime
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import Admin, CustomUser,Staffs,Courses,Students, Subjects #using relitive path (python 3)

#_______________________________________________
# Template Load Methods
#_______________________________________________
def admin_home(request):
    #load the template as django view
    return render(request,"admin_template/home_content.html")

def student_home(request):
    userID = request.user.id
    student = Students.objects.get(admin_id =userID)
    subjects = Subjects.objects.all()
    return render(request,"student_template/home_content.html",{"student":student, "subjects":subjects})

def add_staff(request):
    return render(request,"admin_template/add_staff_template.html")

def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"admin_template/manage_staff_template.html",{"staffs":staffs})

def edit_staff(request,staff_id): # second parameter for url parameter
    # finding staff with parsed url pattern variable
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"admin_template/edit_staff_template.html",{"staff":staff})

def add_course(request):
    return render(request,"admin_template/add_course_template.html")

def manage_course(request):
    courses=Courses.objects.all()
    return render(request,"admin_template/manage_course_template.html",{"courses":courses})

def edit_course(request,course_id): # second parameter for url parameter
    # finding staff with parsed url pattern variable
    course=Courses.objects.get(course_id=course_id)
    return render(request,"admin_template/edit_course_template.html",{"course":course})

def add_student(request):
    courses=Courses.objects.all() #get courses for template page tag
    #calling template render and passing course list to the django tag
    return render(request,"admin_template/add_student_template.html",{"courses":courses})

def register_student(request):
    courses=Courses.objects.all() #get courses for template page tag
    #calling template render and passing course list to the django tag
    return render(request,"student_template/add_student_template.html",{"courses":courses})

def manage_student(request):
    students=Students.objects.all()
    return render(request,"admin_template/manage_student_template.html",{"students":students})

def edit_student(request,student_id): # second parameter for url parameter
    # finding staff with parsed url pattern variable
    student=Students.objects.get(admin=student_id)
    return render(request,"admin_template/edit_student_template.html",{"student":student})

def add_subject(request):
    courses=Courses.objects.all() #get course List for template page tag
    staffs=CustomUser.objects.filter(user_type=2) #filter method (used for targeting single attribute)
    subjects=Subjects.objects.all()
    #calling template render and passing course list to the django tag
    return render(request,"admin_template/add_subject_template.html",{"courses":courses,"staffs":staffs,"subjects":subjects})

def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request,"admin_template/manage_subject_template.html",{"subjects":subjects})

def edit_subject(request,subject_id): # second parameter for url parameter
    # finding staff with parsed url pattern variable
    subject=Subjects.objects.get(subject_id=subject_id)
    return render(request,"admin_template/edit_staff_template.html",{"subject":subject})


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

def register_student_save(request):
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
            return HttpResponseRedirect("/register_student")
        except:
            messages.error(request,"Failed to add user. Please Ensure all fields are correct")
            return HttpResponseRedirect("/")

def edit_staff_save():
    return None

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("Post Method Not Allowed")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Subjects(subject_name=subject_name,staff_id=staff,course_id=course)
            subject.save()
            messages.success(request,"Subject Successfully Added")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request,"Failed to add Subject. Please try again")
            return HttpResponseRedirect("/add_subject")
