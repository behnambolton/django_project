"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include #new
from django.conf.urls.static import static
from project import settings
from pages import views, AdminViews

urlpatterns = [
    path('test/', views.showTestPage),
    path('admin/', admin.site.urls),
    path('', views.showLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('doLogin', views.doLogin),
    path('admin_home', AdminViews.admin_home),
    path('add_staff', AdminViews.add_staff),
    path('add_course', AdminViews.add_course),
    path('add_student',AdminViews.add_student),
    path('add_subject',AdminViews.add_subject),
    path('add_staff_save', AdminViews.add_staff_save),
    path('add_course_save', AdminViews.add_course_save),
    path('add_student_save', AdminViews.add_student_save),
    path('add_subject_save', AdminViews.add_subject_save),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
