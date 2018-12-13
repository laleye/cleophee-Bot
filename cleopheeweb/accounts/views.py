from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def login(request):
    return render(request, 'accounts/login.html')


def base(request):
    return render(request, 'accounts/base.html')
