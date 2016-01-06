from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.view.html')

def register(request):
    return render(request, 'register.view.html')

def userpage(request):
    return render(request,'userpage.view.html')

def events(request):
    return render(request, 'eventslist.view.html')

def error404(request):
		return render(request, '404.view.html')

def error500(request):
		return render(request, '500.view.html')
