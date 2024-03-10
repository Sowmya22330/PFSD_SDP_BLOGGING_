import re

from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect

from .forms import UserForm, BlogForm
from .models import User, Blog
import re
from django.contrib import messages
from django.shortcuts import render, redirect
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

def main(request, username):
    return render(request, 'main.html', {'username': username})

def food(request):
    return render(request, 'food.html')

def travel(request):
    return render(request, 'travel.html')

def create(request):
    return render(request, 'create.html')

def yourblogs(request):
    return render(request, 'yourblogs.html')

def allblogs(request, username):
    blogs = Blog.objects.all()
    return render(request, 'allblogs.html',  {'blogs': blogs, 'username': username})

def register_user(request):
    if request.method == 'POST':
        # Get form data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Regular expressions for input validation
        username_regex = r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$'
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        password_regex = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        # Validate username format
        if not re.match(username_regex, username):
            messages.error(request, "Username should contain a mix of letters and numbers")
            return redirect('/newuser')

        # Validate email format
        if not re.match(email_regex, email):
            messages.error(request, "Invalid email format")
            return redirect('/newuser')

        # Validate password format
        if not re.match(password_regex, password):
            messages.error(request,
                           "Password should be at least 8 characters long and contain letters, numbers, and special characters")
            return redirect('/newuser')

        try:
            # Check if username or email already exists in the database
            existing_user = User.objects.filter(username=username).exists()
            existing_email = User.objects.filter(email=email).exists()

            if existing_user:
                messages.error(request, "Username already exists")
                return redirect('/newuser')

            if existing_email:
                messages.error(request, "Email already exists")
                return redirect('/newuser')

            # Create a new User object with the form data
            new_user = User(username=username, email=email, password=password)

            # Save the user object to the database
            new_user.save()

            # Redirect to a success page or any other page
            messages.success(request, "New account created, login to continue")
            return redirect('/signup')

        except Exception as e:
            messages.error(request, str(e))
            return redirect('/newuser')

    else:
        # Pass any existing messages to the template context
        messages.get_messages(request)

        # Handle GET request if needed
        return render(request, 'newuser.html')
def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Custom authentication logic
        user = authenticate_user(username, password)

        if user is not None:
            # Authentication successful
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect(f'/main/{username}')
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return render(request, 'signup.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')


def authenticate_user(username, password):
    try:
        # Retrieve the user from the database based on the provided username
        user = User.objects.get(username=username)

        # Check if the provided password matches the user's password
        if user.password == password:
            return user
        else:
            return None  # Password doesn't match
    except User.DoesNotExist:
        return None  # User with the provided username doesn't exist
def new(request, username):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('main', username=username)
    else:
        form = BlogForm()

    # Pass the username to the template context
    context = {'form': form, 'username': username}
    return render(request, 'your blogs.html', context)


