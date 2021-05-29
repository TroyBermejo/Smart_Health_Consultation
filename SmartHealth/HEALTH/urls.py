from . import views
from django.urls import path

app_name = 'HEALTH'


urlpatterns = [
    path('login', views.LoginPage.as_view(),name="login"),
    path('patientregister', views.PatientRegister.as_view(),name="patientregister"),
    path('editPatientInformation/<uname>', views.EditPatientInformation.as_view(), name="editPatientInformation"),
    path('editProfile/<uname>', views.EditProfileViews.as_view(), name="editProfile"),


]