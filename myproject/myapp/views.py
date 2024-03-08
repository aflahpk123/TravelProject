from django.shortcuts import render
from.models import Picture

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    obj1=Picture.objects.all()
    return render(request,'index.html',{'result':obj1})

def about(request):
    return render(request,'about.html')