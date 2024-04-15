#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth


def index(request):
    return render(request ,'pages/index.html')
    #template=loader.get_template('pages/index.html')
    #return HttpResponse( template.render )

def register(request):
    
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    context = { 'registerform':form}
    return render(request ,'account/register.html',context=context)

def login(request):
    form=LoginForm()
    if request.method =="POST":
        form = CreateUserForm(request, data=request.POST)
        if form.is_valid()():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("'account/dashboard.html'")
    context= { 'LoginForm':form}
    return render(request, 'account/login.html', context=context)
def dashboard(request):
    return render(request ,'account/dashboard.html')
       
    
def signup(request):
    return render(request ,'account/signup.html')

def association(request):
    return render(request ,'account/association.html')
    
def logout(request):
    
    # Call Django's logout function
    django_logout(request)
    return redirect("")
    #return render(request ,'account/logout.html')
    
#def about(request):
    #return HttpResponse('about page')
    #return render(request,'pages/about.html')