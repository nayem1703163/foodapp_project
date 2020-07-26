from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from User.forms import UserCreationFormExtended,UserProfileForm
# Create your views here.____________
def signup_user(request):
    if request.method=='POST':
        form = UserCreationFormExtended(request.POST)
        profile = UserProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user= form.save()
            p = profile.save(commit=False)
            p.user = user
            p.save()
            grahok = login(request,user)
            if(user.userprofile.check == 'khadok'):
                return redirect("reslist")
            if(user.userprofile.check == 'rider'):
                return HttpResponse('This is rider')
            if(user.userprofile.check == 'store'):
                return HttpResponse('This is store')

    else:
        form = UserCreationFormExtended()
        profile = UserProfileForm()
        return render(request,"User/signup.html",{"form":form,"profile" : profile})


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

