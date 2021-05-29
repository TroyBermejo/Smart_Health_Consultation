from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from django.views.generic.base import View
from .models import Appointment
from .forms import AppointmentForm

class IndexView(View):
    template_name = "SMART/index.html"

    def get(self, request):
        return render(request, self.template_name)

class IndexLoginView(View):
    template_name = "SMART/indexLogin.html"

    def get(self, request):
        return render(request, self.template_name)


class CheckingUpView(View):
    template_name = "SMART/checkUp2.html"

    def get(self, request):
        return render(request, self.template_name)


class ViewDoctor(View):
    template_name = "SMART/doctor2.html"

    def get(self, request):
        return render(request, self.template_name)


class SingleDoctor(View):
    template_name = "SMART/doctor-single2.html"

    def get(self, request):
        return render(request, self.template_name)


class AppointmentView(View):
    template_name = "SMART/appointment2.html"

    def get(self, request):
        return render(request, self.template_name)


class ViewDepartment(View):
    template_name = "SMART/department2.html"

    def get(self, request):
        return render(request, self.template_name)


class ViewDepartmentSingle(View):
    template_name = "SMART/department-single2.html"

    def get(self, request):
        return render(request, self.template_name)

class ViewBlogSidebar(View):
    template_name = "SMART/blog-sidebar2.html"

    def get(self, request):
        return render(request, self.template_name)

class ViewBlogSingle(View):
    template_name = "SMART/blog-single2.html"

    def get(self, request):
        return render(request, self.template_name)

class ViewService(View):
    template_name = "SMART/service2.html"

    def get(self, request):
        return render(request, self.template_name)


class ViewAbout(View):
    template_name = "SMART/about2.html"

    def get(self, request):
        return render(request, self.template_name)


class ViewContact(View):
    template_name = "SMART/contact2.html"

    def get(self, request):
        return render(request, self.template_name)














class ServiceView(View):
    template_name = "SMART/service.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})

class AboutView(View):
    template_name = "SMART/about.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})

class ContactView(View):
    template_name = "SMART/contact.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})

class DoctorView(View):
    template_name = "SMART/doctor.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})

class DoctorSingleView(View):
    template_name = "SMART/doctor-single.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})

class DepartmentView(View):
    template_name = "SMART/department.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})

class DepartmentSingleView(View):
    template_name = "SMART/department-single2.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})




class ConfirmationView(View):
    template_name = "SMART/confirmation.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})


class DashboardView(View):
    template_name = "SMART/dashboard.html"

    def get(self, request):
        appointment = Appointment.objects.all()
        return render(request, self.template_name, {'appointment': appointment})


class BlogSingleView(View):
    template_name = "SMART/blog-single.html"
    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})


class BlogSideBarView(View):
    template_name = "SMART/blog-sidebar.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})


class CheckUpView(View):
    template_name = "SMART/checkUp.html"

    def get(self, request,uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})


class LoggedInView(View):
    template_name = "SMART/indexLogin.html"

    def get(self, request, uname):
        print(uname)
        return render(request, self.template_name, {'uname': uname})


class makeAppointment(View):
    template_name ="SMART/appointment.html"

    def get(self, request, uname):
        print(uname)
        formAppointment = AppointmentForm()
        return render(request, self.template_name,{'formAppointment' :formAppointment})

    def post(self, request, uname):
        print(uname)
        formAppointment = AppointmentForm(request.POST)

        if formAppointment.is_valid():
            Appointment = formAppointment.save(commit=False)
            Appointment.save()
            return redirect(reverse('SMART:confirmation', kwargs={'uname' :uname}))

        context = {'formPatient': formPatient}
        return render(request, self.template_name, context)


class AppointmentViews(View):
    template_name = "SMART/dashboard.html"

    def get(self, request, uname):
        appointment = Appointment.objects.all()
        return render(request, self.template_name, {'appointment': appointment, 'uname': uname})

