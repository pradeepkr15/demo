from django.shortcuts import render, HttpResponseRedirect
from adminApp.forms import EditForm, UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    if request.user.is_superuser:
                        return HttpResponseRedirect('/admin/')
                    return HttpResponseRedirect('/dashboard/')       
        else:    
            fm = LoginForm()
        context = {'form':fm}
        return render(request, "adminApp/account/login.html", context)

def registerPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method == "POST":
            fm = UserRegistrationForm(request.POST)
            if fm.is_valid():
                fm.save()
                obj = User.objects.get(username=fm.cleaned_data['username'])
                user_obj = UserProfile.objects.create(user=obj)
                user_obj.save()
                messages.success(request, 'Account created successfully..!!')
        else:
            fm = UserRegistrationForm()

        context = {'form':fm}
        return render(request, 'adminApp/account/register.html', context)

def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST['data']
            print(data)
        return render(request, "adminApp/admin/dashboard.html")
    else:
        return HttpResponseRedirect('/')

def blank_page(request):
    if request.user.is_authenticated:
        return render(request, 'adminApp/admin/blank-page.html')
    else:
        return HttpResponseRedirect('/')

def userProfile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        udata = UserProfile.objects.filter(user=user).first()
        if request.method == 'POST':
            profile_fm = EditProfileForm(data=request.POST, instance=udata)
            if profile_fm.is_valid():
                profile_fm.save()
                messages.success(request, 'Profile has been successfully updated..!!')
        else:
            profile_fm = EditProfileForm(instance=udata)
        context = {'user':user, 'udata':udata, 'profile_form':profile_fm}
        return render(request, 'adminApp/admin/profile.html', context)
    else:
        return HttpResponseRedirect('/')

def student(request):
    if request.user.is_authenticated:
        std_objs = Student.objects.all()
        context = {'std_objs':std_objs}
        return render(request, 'adminApp/admin/student.html', context)
    else:
        return HttpResponseRedirect('/')





