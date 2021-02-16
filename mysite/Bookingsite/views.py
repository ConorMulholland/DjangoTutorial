from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'bookingsite/login.html')

def success(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'Bookingsite/Welcome.html')
    else:
        return HttpResponseRedirect(reverse('Bookingsite:home'))