from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request , 'home/index.html')

def about(request):
    return render(request , 'home/about.html')

def tut(request):
    return render(request , 'home/tuts.html')