from django.shortcuts import render, redirect
# from .forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def UserLogin(request):
    error_message = ''
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user:
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request,user)
                    return redirect('home')
                else:
                    error_message = 'Username and password doesnot match!'
            
        except:
            error_message = "User doesnot exists!"
        
    context = {'error_message':error_message, 'page':page}
    return render(request, 'accounts/login.html', context)

def UserLogout(request):
    logout(request)
    return redirect('login')

def UserSignUp(request):

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        username = email.split('@gmail.com')[0]
        password = make_password(password=request.POST.get('password'))

        user = User.objects.create(username=username, password=password, first_name=firstName, last_name=lastName, email=email)
        login(request,user)
        return redirect('home')

    return render(request, 'accounts/signup.html')