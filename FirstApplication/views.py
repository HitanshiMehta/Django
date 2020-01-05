from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'hitanshi'})

def Add(request):
    val1=int(request.POST['No1'])
    val2=int(request.POST['No2'])
    res=val1+val2
    return render(request, 'result.html',{'res':res})