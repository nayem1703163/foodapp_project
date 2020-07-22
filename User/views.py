from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def signup_user(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #loged in
            return redirect("reslist")
    else:
        form = UserCreationForm()
    return render(request,"User/signup.html",{"form":form})
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # loged in __
            return redirect("reslist")
    else:
        form = AuthenticationForm()
    return render(request, "User/login.html", {"form": form})
