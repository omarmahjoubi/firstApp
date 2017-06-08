from django.shortcuts import render
from django.shortcuts import redirect

import hashlib
from inventory import views

from .forms import UserForm
from .models import User

def sign_up(request) :
    if request.method == "POST" :
        form = UserForm(request.POST)
        print("email ===> {0}".format(request.POST))

        if form.is_valid() :
            print("i'm here")
            user = form.save(commit=False)
            user.password = hashlib.sha256(user.password).hexdigest()
            user.save()
            request.session['connected']=True
            request.session['user_email']=user.email
            return redirect('/')
        else :
            return render (request,'auth/sign_up.html',{ 'form': form})
    else :
        print("i'm not here")
        form = UserForm()
        return render(request,'auth/sign_up.html',{ 'form' : form })

def log_out(request):
    request.session['connected']=False
    del request.session['user_email']
    return redirect('/')

def login(request):
    if request.method == "POST" :
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = hashlib.sha256(user.password).hexdigest()
            result = User.objects.filter(email=user.email).filter(password=user.password)
            if not result :
                return render(request,"auth/login.html", {"msg" : "incorrect credentials" , "form" : form})
            else :
                request.session['connected'] = True
                request.session['user_email']= user.email
                return redirect('/')
        else :
            return render(request,"auth/login.html", { "form" : form})
    else :
        form = UserForm()
        return render(request, "auth/login.html", {"form": form})




