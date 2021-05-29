from django.db import models

# Create your models here.

GENDER_CHOICES = [('M', 'Male'),
                  ('F', 'Female')]

MARITAL_CHOICES = [('S', 'Single'),
                   ('M', 'Married'),
                   ('W', 'Widow/Widower')]


class Account(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    middleinitial = models.CharField(max_length=1)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Patient(Account):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    province = models.CharField(max_length=20)
    barangay = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    maritalstatus = models.CharField(max_length=1, choices=MARITAL_CHOICES)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
