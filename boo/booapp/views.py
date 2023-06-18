from django.shortcuts import render,redirect
from django.http import HttpResponse
from .function import ufile
from . models import abi

# Create your views here.
def home(request):
   
    mydata=abi.objects.all()
    if mydata !='':
         return render(request,'index.html',{'datas':mydata})
    else:
        return render(request,'index.html')


def adddata(request):
    if request.method =="POST":
        name=request.POST['mob']
        con=request.POST['keyboard']
        obj=abi()
        obj.mobile=name
        obj.keyboard=con
        obj.save()
        mydata=abi.objects.all()
        return redirect('home')
    return render(request,'index.html')
  

def update(request,id):
    c=abi.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST['mob']
        con=request.POST['keyboard']
        c.mobile=name
        c.keyboard=con
        c.save()
        return redirect('home')
        
    
    return render(request,'update.html',{'data':c})


def delete(request,id):
     c=abi.objects.get(id=id)
     c.delete()
     return redirect('home') 
