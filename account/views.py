from account.decorators import unauthenticated_user
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages


@unauthenticated_user
def login_page(request):
    """ This function check group and login user to system and redirect to home page of each group """

    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            request.session.set_expiry(3600)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is Incorrect')

    return render(request, 'account/login.html')


def logout_user(request):
    """ Function to log out user """

    logout(request)
    return redirect('login')

