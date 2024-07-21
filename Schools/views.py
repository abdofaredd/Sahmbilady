from django.shortcuts import render
from django.http import HttpResponse
from Schools.models import School
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse('Hello world');
def index(request,id):
    school=School.objects.get(id=id)
    return render(request, 'index.html',{'school':school})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')