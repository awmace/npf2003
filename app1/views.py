from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print('这是第一个试图')
    return HttpResponse('Success')

def demo(request):
    print('这是div分支上的代码')
    return HttpResponse('123')
