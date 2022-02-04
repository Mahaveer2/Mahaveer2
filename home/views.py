from django.shortcuts import render
from django.http import HttpResponse
from home.models import Posts

# Create your views here.
def index(request):
    context = {'data':Posts.objects.all()}
    return render(request , 'home/index.html',context)

def about(request):
    return render(request , 'home/about.html')

def tut(request):
    return render(request , 'home/tuts.html')