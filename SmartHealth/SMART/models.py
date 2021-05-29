from django.db import models

class Appointment(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    doctor = models.CharField(max_length=90)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname
