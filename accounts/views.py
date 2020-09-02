from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
# Create your views here.

def login_view(request) :
    if request.method == "POST" :
        userid = request.POST["userid"]
        password = request.POST['password']
        user = authenticate(userid=userid, password=password)
        if user is not None :
            print("인증성공")
            login(request. user)
        else :
            print("인증실패")
    return render(request, "intro.html")


def logout_view(request) : 
    logout(request)
    return redirect("accounts:login")

def register_view(request) : 
    if request.method == 'POST' :
        print(request.POST)
        userid = request.POST["userid"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]   

        user = User.objects.create_user(userid, password)
        user.lastname = lastname
        user.firstname = firstname
        user.save()

        return redirect("accounts:login")
        
    return render(request, "register.html")