from django.shortcuts import render,redirect
from .models import *
from .forms import Obraform

def home(request):
    return render(request,'index.html')

def crearObra(request):
    if request.method=='POST':
        form=Obraform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Obraform()
        return render(request,'pagweb/crear_obra.html',{'form':form})
