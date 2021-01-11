from django.http import response
from django.urls import reverse
from django.test import TestCase, Client
from pages.models import CustomUser,Staffs,Students,Admin,Subjects,Courses,FeedBackStudent,NotificationStaff,NotificationStudent
from pages import AdminViews
from pages import urls

# Create your tests here.
class TestDBModels(TestCase):

    def testDBModels(self):
        self.user = CustomUser.objects.create(id=1)
        self.staff = Staffs.objects.create(admin_id=1, address = 'TestAddress')
        self.course = Courses.objects.create(course_name= 'TestCourse')
        self.subject = Subjects.objects.create(
            subject_name = 'TestSubject',
            course_id_id = 1,
            staff_id_id = 1
        )

        # Testing that the DB Model Persists
        self.assertEquals(self.subject, Subjects.objects.get(id=1))
        self.assertEquals(self.user, CustomUser.objects.get(id=1))
        self.assertEquals(self.staff, Staffs.objects.get(id=1))
        self.assertEquals(self.subject, Subjects.objects.get(id=1))
        
        # Testing that the Model has properties
        self.assertIn('TestSubject', self.subject.subject_name)
        self.assertIn('TestCourse', self.course.course_name)
        self.assertIn('TestAddress', self.staff.address)

class TestAppViews(TestCase):
    
    def testHomeRender(self):
        self.client = Client()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def testRegistrationRender(self):
        self.client = Client()
        response = self.client.get("/register_student")
        self.assertEqual(response.status_code, 200)

    def testSucessLoginUrlRedirect(self):
        self.client = Client()
        response = self.client.post('/doLogin', {"email": "admin@mail.com", "password": "Password123!"})
        self.assertEquals(response.status_code, 302) #sucessfull redirect
        self.assertRedirects(response, '/')

    def testAuthentication(self):
        user = CustomUser.objects.create(id=1, email='admin@mail.com',password='Password123!',username='user')
        user.save
        self.client = Client()
        self.response = self.client.login(username='admin@mail.com', password='Password123!')
        self.assertEqual(self.response, False)