from .forms import Bookform
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .filters import *
# Create your views here.

def form(request):
    if request.method=='POST':
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/display')
    else:
        form=Bookform
    return render(request, 'book/form.html',{
        'form':form
    })

        

def display(request):
    display_list=Book.objects.all()
    return render(request, 'book/disp.html',{
       'display_list'  : display_list
     })

def filter(request):
    f = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'book/filt.html', {'filter': f})