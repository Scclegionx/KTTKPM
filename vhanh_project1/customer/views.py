from django.shortcuts import render
from .models import Customer

def profile(request):
    return render(request, 'customer/profile.html')
