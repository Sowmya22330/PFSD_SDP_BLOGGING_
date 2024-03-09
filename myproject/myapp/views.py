
from django.shortcuts import render, redirect

from myproject.myapp.models import User


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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # You might want to create a UserProfile instance as well if needed
        # user_profile = UserProfile.objects.create(user=user, other_fields=values)

        # Optionally, you can also login the user after registration
        # login(request, user)

        return redirect('signup')  # Redirect to login page after successful registration

    return render(request, 'registration/register.html')