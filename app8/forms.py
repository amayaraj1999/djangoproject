from dataclasses import field, fields
from django import forms
from . models import Table1,Image

class Table1Form(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    class Meta():
        model=Table1
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    class Meta():
        model=Table1
        fields=('Email','Password')

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Table1
        fields=('Name','Age','Place')    

class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    ConfirmNewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)

class ImageForm(forms.ModelForm):
    class Meta():
        model=Image()
        fields='__all__'