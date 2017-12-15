'''
Created on 2017年12月14日

@author: user
'''

from django.http import HttpResponse

'''
def hello(request):
    return HttpResponse("Hello world ! ")
'''
from django.shortcuts import render
 
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)