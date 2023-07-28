from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from flights .models import Passenger


from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate ,login ,logout 

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request,"users/user.html")







def login_view(request):
   if request.method=="POST":
       username=request.POST["name"]
       password=request.POST["password1"]
       user =authenticate(request,username=username,password=password)
       print (user)
       if user is not None:
           login(request,user)
           return HttpResponseRedirect(reverse("users:index"))
       else :
          return render(request,"users/login.html",{"message":"invalid data."})      

   return render(request,'users/login.html')



def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{"message":"you'r logged out "})



def sign_up(request):
     if request.method == 'POST':
        username = request.POST['fname']
        lastname = request.POST['lname']

        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username=='' or email==''or password1==''or password2=='':
            messages.info(request, 'Requierd Fields')
            return redirect('/users/sign_up/')
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/users/sign_up/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/users/sign_up/')
            else:
                 user = User.objects.create_user(username=username, email=email, password=password1,first_name=username, last_name=lastname)
                 user.save() 
                 print ("dddddddd")
                 user_model=User.objects.get(username=username)
                 new_passenger = Passenger.objects.create(first=user_model.first_name,last=user_model.last_name)
                 new_passenger .save()
                 messages.success(request, 'Thanks to join')

                 return redirect('')
     else:  
              return render(request,'users/sign_up.html')    
