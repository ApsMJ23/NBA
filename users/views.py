from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
    