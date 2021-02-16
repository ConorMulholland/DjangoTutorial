from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def myview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login/Welcome.html')
    else:
        return HttpResponseRedirect(reverse('login:index'))