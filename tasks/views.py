from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def maanger_dashboard(request):
    return render(request, "dashboard/maanger.html")  # ei line change


def jk(request):
    return render(request,"jk.html")
def second_page(request):
    return render(request, "dashboard/2nd.html")

def test(request):
    return render(request,'test.html')

def test_2(request):
    context={
        'name' :["Mahmud","Ahmed","john"],
        'age'  :23

    }
    return render(request,'test.html',context)
def test_3(request):
    context={
        'names' :["Mahmud","Ahmed","john",'smith'],
        'age'  :23

    }
    return render(request,'test.html',context)


