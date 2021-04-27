from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
        return render(request, "users/index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(request , username= username, password = password)
        if auth is not None:
            login(request,auth)
            return HttpResponseRedirect(reverse("team:index"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid Credentials"
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
                "message": "Logged Out Successfully!!"})
    