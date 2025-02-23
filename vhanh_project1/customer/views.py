from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm

def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form data")
    else:
        form = LoginForm()

    return render(request, "customer/login_register.html", {"form": form, "page": "login"})

def register_page(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Registration failed")
    else:
        form = RegisterForm()

    return render(request, "customer/login_register.html", {"form": form, "page": "register"})

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect("login")




@login_required(login_url='login')
def profile(request):
    return render(request, 'customer/profile.html')