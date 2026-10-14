from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # pore shob kaj korbo
    # work with database
    # transform data
    # data pass
    # Http response/json respon
    return HttpResponse("hi,bye")

def contact(request):
    return HttpResponse(' <h1> This is contact page </h1>')

def show_task(request):
    return HttpResponse('<h1>This is in task page --> show_task </h1>')

def show_specific_task(request, id):
    print(f'{id}')
    print(f'id type {type(id)}')
    return HttpResponse('This is specific task page')

def dashboard(request,id):
    return HttpResponse('This is in dashboard')