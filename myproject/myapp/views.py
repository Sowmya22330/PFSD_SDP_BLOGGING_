import re

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import  UserForm
from .models import User


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

def food(request):
    return render(request, 'food.html')

def travel(request):
    return render(request, 'travel.html')

def create(request):
    return render(request, 'create.html')

def register_user(request):
    if request.method == 'POST':
        # Get form data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username starts with an alphabet
        if not re.match("^[a-zA-Z]", username):
            messages.error(request, "Username must start with an alphabet")
            return redirect('/signup')

        # Check if email ends with "@gmail.com"
        if not email.endswith("@gmail.com"):
            messages.error(request, "Email must end with @gmail.com")
            return redirect('/signup')

        # Check if password contains at least one uppercase letter, one special character, and one digit
        if not re.match("^(?=.*[A-Z])(?=.*[@#$%^&+=])(?=.*\d).*$", password):
            messages.error(request, "Password must contain at least one uppercase letter, one special character, and one digit")
            return redirect('/signup')

        # Create a new User object with the form data
        new_user = User(username=username, email=email, password=password)

        # Save the user object to the database
        new_user.save()

        # Redirect to a success page or any other page
        messages.success(request, "New account created, login to continue")
        return redirect('/signup')

    else:
        # Pass any existing messages to the template context
        messages.get_messages(request)

        # Handle GET request if needed
        return render(request, 'signup.html')
