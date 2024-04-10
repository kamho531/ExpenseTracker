from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from book.models import Book
from .forms import SignUpForm



# Create your views here.
def home(request):
    books = Book.objects.all()
    # check if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've just logged in!")
            return redirect('home')
        else:
            messages.success(request, "Error! please try again!")
            return redirect('home')
    else:        
        return render(request, 'home/home.html', 
                  {'books': books})



def userlogout(request):
    logout(request)
    messages.success(request, "You have logged out!")
    return redirect('home')


def usersignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration success")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'home/signup.html', 
                  {'form': form})
    
    return render(request, 'home/signup.html', 
                  {'form': form})

