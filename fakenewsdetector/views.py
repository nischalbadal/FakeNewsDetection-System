from django.shortcuts import render
import requests

import sys
from subprocess import run,PIPE

def button(request):
   return render(request,'home.html')

def external(request):
    input = request.POST.get('news')

    print(out)
    return render (request, 'home.html',{'data1':out})