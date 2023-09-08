from django.shortcuts import render

# Create your views here.

def alert(request):
    return render(request,'alert.html')

def badge(request):
    return render(request,'badge.html')

def breadcrumb(request):
    return render(request,'breadcrumb.html')


def button(request):
    return render(request,'button.html')