from django.shortcuts import render
import requests

import sys
from subprocess import run,PIPE

def button(request):
   return render(request,'home.html')

