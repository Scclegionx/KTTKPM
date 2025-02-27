from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm, CustomerProfileForm
from django.contrib.auth.decorators import login_required
from base.utils import get_tokens_for_user

def customer_register(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save(using='mysql_db')
            login(request, user, backend='customer.backends.CustomerAuthBackend')
            return redirect("customer_profile")
        else:
            messages.error(request, "Registration failed")
    else:
        form = RegisterForm()

    return render(request, "customer/login_register.html", {"form": form, "page": "register"})


def customer_login(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                login(request, user, backend='customer.backends.CustomerAuthBackend')
                tokens = get_tokens_for_user(user, 'customer.backends.CustomerAuthBackend')

                # Lưu token vào session
                request.session['access_token'] = tokens['access']
                request.session['refresh_token'] = tokens['refresh']

                return redirect("customer_profile")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form data")
    else:
        form = LoginForm()

    return render(request, "customer/login_register.html", {"form": form, "page": "login"})

@login_required(login_url="login")
def customer_logout(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def profile(request):
    return render(request, 'customer/profile.html', {"user": request.user})


@login_required
def customer_profile(request):
    customer = request.user
    return render(request, 'customer/profile.html', {'customer': customer})

@login_required
def edit_profile(request):
    customer = request.user
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('customer_profile')
    else:
        form = CustomerProfileForm(instance=customer)
    return render(request, 'customer/edit_profile.html', {'form': form})


# customer/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests

def test_book_access(request):
    if not request.user.is_authenticated:
        return HttpResponse("Bạn chưa đăng nhập", status=401)

    access_token = request.session.get('access_token')

    headers = {'Authorization': f'Bearer {access_token}'}

    # Test GET
    get_response = requests.get('http://127.0.0.1:8000/api/books/', headers=headers)
    print("GET response:", get_response.status_code)

    # Test POST
    post_response = requests.post(
        'http://127.0.0.1:8000/api/books/',
        json={'title': 'Test Book', 'author': 'Test Author', 'price': 100},
        headers=headers
    )
    print("POST response:", post_response.status_code)

    return HttpResponse("Đã test xong, check console")
