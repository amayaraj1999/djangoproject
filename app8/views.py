from unicodedata import name
from django.shortcuts import render,redirect
from django.contrib import messages
from app8.models import Table1
from django.contrib.auth import logout as logouts
from . forms import Table1Form,LoginForm,UpdateForm,ChangePasswordForm,ImageForm
# Create your views here.
def index(request):
    name='amaya'
    return render(request,'index.html',{'data':name})#context

# def show_form(request):
#     if request.method=='POST':
#         form=Table1Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form=Table1Form()
#     return render(request,'show_form.html',{'data':form})#context


# def show_form(request):
#     if request.method=='POST':
#         form=Table1Form(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['Name']
#             age=form.cleaned_data['Age']
#             place=form.cleaned_data['Place']
#             email=form.cleaned_data['Email']
#             password=form.cleaned_data['Password']
#             cpassword=form.cleaned_data['ConfirmPassword']
#             form.save()
#             return redirect('/')
#     else:
#         form=Table1Form()
#     return render(request,'show_form.html',{'data':form})#context



def show_form(request):
    if request.method=='POST':
        form=Table1Form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']

            user=Table1.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Email already exists")
                return redirect('/show_form')
            elif password!=cpassword:
                messages.warning(request,"Password missmatch")
                return redirect('/show_form')
            else:
                tab=Table1(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"Account created")
                return redirect('/')
    else:
        form=Table1Form()
    return render(request,'show_form.html',{'data':form})#context

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=Table1.objects.get(Email=email)

            if not user:
                messages.warning(request,"User doesnot exist")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"Incorrect Password")
                return redirect(' /login')   
            else:
                messages.success(request,"Login successfull")
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})#context

def home(request,id):
    data=Table1.objects.get(id=id)
    return render(request,'home.html',{'data':data})#context


def update(request,id):
    data=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=data)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            form.save()
            messages.success(request,"Update successfully")
            return redirect('/home/%s' % data.id) 
    else:
        form=UpdateForm(instance=data)
    return render(request,'update.html',{'data':data,'form':form})    

def display_users(request):
    users=  Table1.objects.all()
    return render(request,'display.html',{'users':users})    

def delete(request,id):
    data=Table1.objects.get(id=id)
    data.delete()
    messages.success(request,"Delete successfully")
    return redirect('/') 

def change_password(request,id):
    data=Table1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            cnewpassword=form.cleaned_data['ConfirmNewPassword']

            if oldpassword!=data.Password:
                messages.warning(request,"Password are different")
                return redirect('/change_password/%s' % data.id)
            elif oldpassword==newpassword:
                messages.warning(request,"Both the passwords are similar")
                return redirect('/change_password/%s'% data.id)    
            elif newpassword!=cnewpassword:
                messages.warning(request,"Password doesnot match ")
                return redirect('/change_password/%s' % data.id)  
            else:
                data.Password=newpassword
                data.save()
                messages.success(request,"Password changed successfully") 
                return redirect('/home/%s' % data.id)  
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'data':data,'form':form})


def logout(request):
    logouts(request)
    messages.success(request,"Logout successfully")
    return redirect('/')


def image(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"image added successfully")
            return redirect('/')
    else:
        form=ImageForm()
    return render(request,'image.html',{'form':form})            