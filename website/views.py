from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username = username, password = password)
        return check_user_exists(request, user)

    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    return render(request, "register.html", {})

# Utility Functions -------------------------------------------------------

def check_user_exists(request, user):
    if user is not None:
        login(request, user)
        return show_message(request, "You Have Been Logged In!")
    else:
        return show_message(request,
                            "There was an error, please try again.")

def show_message(request, msg):
    messages.success(request, msg)
    return redirect('home')
