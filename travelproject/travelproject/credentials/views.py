from django.contrib import messages,auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request,"login.html")
         if request.method == 'POST':
             username = request.POST['username']
             password = request.POST['password']
             user=auth.authenticate(username=username,password=password)

         if user is  not None:
            auth.login(request,user)
            return redirect('/')
         else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")


def register(request,email=None):
    global user
    if request.method == 'POST':
        username = request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                  user=User.objects.create_user(username = user_name, password = password, firstname =first_name, lastname =last_name, email=email)
                  user.save();
                  return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def logout(request):
    auth.login(request)
    return render('/')