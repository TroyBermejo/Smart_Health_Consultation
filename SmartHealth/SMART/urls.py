from . import views
from django.urls import path

app_name = 'SMART'


urlpatterns = [
    path('index', views.IndexView.as_view(),name="index"),
    path('indexLogin', views.IndexLoginView.as_view(), name="indexLogin"),
    path('Doctor', views.ViewDoctor.as_view(), name="Doctor"),
    path('Doctorsingle', views.SingleDoctor.as_view(), name="Doctorsingle"),
    path('Appointment', views.AppointmentView.as_view(), name="Appointment"),
    path('checkUp', views.CheckingUpView.as_view(), name="checkUp"),
    path('Department', views.ViewDepartment.as_view(), name="Department"),
    path('Departmentsingle', views.ViewDepartmentSingle.as_view(), name="Departmentsingle"),
    path('Blogsidebar', views.ViewBlogSidebar.as_view(), name="Blogsidebar"),
    path('Blogsingle', views.ViewBlogSingle.as_view(), name="Blogsingle"),
    path('Service', views.ViewService.as_view(), name="Service"),
    path('About', views.ViewAbout.as_view(), name="About"),
    path('Contact', views.ViewContact.as_view(), name="Contact"),


############################################################################################################################


    path('service/<uname>', views.ServiceView.as_view(), name="service"),
    path('about/<uname>', views.AboutView.as_view(), name="about"),
    path('contact/<uname>', views.ContactView.as_view(), name="contact"),
    path('checkup/<uname>', views.CheckUpView.as_view(), name="checkup"),
    path('doctor/<uname>', views.DoctorView.as_view(), name="doctor"),
    path('doctorsingle/<uname>',views.DoctorSingleView.as_view(), name="doctorsingle"),
    path('department/<uname>',views.DepartmentView.as_view(), name="department"),
    path('departmentsingle/<uname>',views.DepartmentSingleView.as_view(),name="departmentsingle"),
    path('dashboard/<uname>',views.AppointmentViews.as_view(),name="dashboard"),
    path('appointment/<uname>',views.makeAppointment.as_view(), name="appointment"),
    path('confirmation/<uname>',views.ConfirmationView.as_view(), name="confirmation"),
    path('blogsingle/<uname>',views.BlogSingleView.as_view(), name="blogsingle"),
    path('blogsidebar/<uname>',views.BlogSideBarView.as_view(), name="blogsidebar"),
    path('indexLogin/<uname>', views.LoggedInView.as_view(), name="indexLogin"),


]