from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_user(request):
    form = UserCreationForm()
    return render(request,"User/signup.html",{"form":form})
def login_user(request):
    return render(request,'user/login.html')
