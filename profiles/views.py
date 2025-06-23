from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # or any success page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password. Please try again.'})

    return render(request, 'login.html', {})




def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists. Please choose another.'
            })

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # log them in right after register
        return redirect('home')  # or wherever you want to go

    return render(request,'register.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')