from django.shortcuts import render
from fakenews.prediction import detecting_fake_news
import requests
import sys

# Create your views here.

def index(request):
    outputlist=[]
    
    input = request.POST.get('news')
    
    outputlist=detecting_fake_news(input)
    return render (request, 'home.html',{'data0':input,'data1':outputlist[0],'data2':outputlist[1],'percentage':outputlist[1]*100})