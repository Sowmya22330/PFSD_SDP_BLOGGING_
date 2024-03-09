
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')

def newuser(request):
    return render(request, 'newuser.html')

def steps(request):
    return render(request, 'steps.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def main(request):
    return render(request, 'main.html')
