from django.shortcuts import render, redirect
from . import forms
from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
# Create your views here.



# def index(request):
#     return redirect(home')
# def homepage(request):
#     return render(request,'home.html')

class HomePageView(TemplateView):
    template_name='home.html'




def contactus(request):
    if request.method=='POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.ContactUsForm()
    context = {
        'form':form
    }
    return render(request,'contact.html',context)



def registration(request):
    if request.method=='POST':

        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = forms.RegistrationForm()
    return render(request,'users/regis.html',{'form':form})



def sing_in(request):
    if request.method=='POST':

        form = forms.LoginForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = forms.LoginForm()
    return render(request,'users/login.html',{'form':form})   
    
