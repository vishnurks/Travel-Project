from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Place
from .models import Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'res': obj1})


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['password1']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email,
                                                password=pwd)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def logout(request):

    auth.logout(request)
    return redirect('/')
