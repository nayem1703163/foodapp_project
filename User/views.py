from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from User.admin import UserCreationFormExtended

# Create your views here.____________
def signup_user(request):
    if request.method=='POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect("reslist")
    else:
        form = UserCreationFormExtended()
    return render(request,"User/signup.html",{"form":form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("reslist")
    else:
        form = AuthenticationForm()
    return render(request, "User/login.html", {"form": form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect("reslist")
#Finish
