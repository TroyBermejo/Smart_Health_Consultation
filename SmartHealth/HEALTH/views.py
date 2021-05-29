
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout

from .forms import AccountForm, PatientForm, LoginForm
from .models import Account, Patient
from django.contrib import messages

class PatientRegister(View):
    template_name="HEALTH/register.html"

    def get(self, request):
        formPatient = PatientForm()
        return render(request,self.template_name,{'formPatient':formPatient})

    def post(self,request):
        formPatient = PatientForm(request.POST)

        if formPatient.is_valid():
            patient = formPatient.save(commit=False)
            patient.save()
            return redirect(reverse('HEALTH:login'))

        return render(request, self.template_name, {'formPatient':formPatient})

class LoginPage(View):
    template_name='HEALTH/login.html'

    def get(self , request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        print ("Username:"+uname)
        error=""
        print("No of record:"+str(Account.objects.filter(pk=uname).count()))
            #select count(*) from account where username='uname'
        if Account.objects.filter(pk=uname).count() != 0:
            account = Account.objects.get(pk=uname)
            if account.password == pwd:
                print("uname"+uname)
                return redirect(reverse('SMART:indexLogin',kwargs={'uname':uname,}))
            else:
                error ="Incorrect password."
        else:
             error="Username does not exist."

        return render(request, self.template_name, {'form': form, 'error':error})


class EditPatientInformation(View):
    template_name = "HEALTH/register.html"

    def get(self, request, uname):
        patient = Patient.objects.get(username=uname)
        formPatient = PatientForm(instance=patient)
        context = {'formPatient': formPatient}
        return render(request, self.template_name, context)

    def post(self, request, uname):
        patient = Patient.objects.get(username=uname)
        if request.method == 'POST':
            formPatient = PatientForm(request.POST, instance=patient)
            if formPatient.is_valid():
                formPatient.save()
                return redirect(reverse('SMART:indexLogin' ,kwargs={'uname' :uname,}))

        context = {'formPatient':formPatient}
        return render(request, self.template_name, context)


class EditProfileViews(View):
    template_name = "HEALTH/editProfile.html"

    def get(self, request, uname):
        patient = Patient.objects.get(username=uname)
        return render(request, self.template_name, {'patient': patient})



