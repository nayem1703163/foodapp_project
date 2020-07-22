from django.shortcuts import render

# Create your views here.
def signup_user(request):
    return render(request,"User/signup.html")
def login_user(request):
    return render(request,'user/login.html')
