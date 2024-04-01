from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    return render(request ,'pages/index.html')
    #template=loader.get_template('pages/index.html')
    #return HttpResponse( template.render )

#def about(request):
    #return HttpResponse('about page')
    #return render(request,'pages/about.html')