from django import forms
from .models import Account, Patient

GENDER_CHOICES = [('M', 'Male'),
                  ('F', 'Female')]

MARITAL_CHOICES = [('S', 'Single'),
                   ('M', 'Married'),
                   ('W', 'Widow/Widower')]


class AccountForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    middleinitial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('__all__')


class PatientForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    middleinitial = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=GENDER_CHOICES,
    )
    maritalstatus = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=MARITAL_CHOICES,
    )
    province = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    barangay = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = ('__all__')


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('username', 'password')