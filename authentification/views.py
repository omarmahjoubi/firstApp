from django.shortcuts import render
from django.shortcuts import redirect

import hashlib
from inventory import views

from .forms import UserForm

def sign_up(request) :
    if request.method == "POST" :
        form = UserForm(request.POST)
        print("email ===> {0}".format(request.POST))

        if form.is_valid() :
            print("i'm here")
            user = form.save(commit=False)
            user.password = hashlib.sha256(user.password).hexdigest()
            user.save()
            return redirect('/')
        else :
            return render (request,'auth/sign_up.html',{ 'form': form})
    else :
        print("i'm not here")
        form = UserForm()
        return render(request,'auth/sign_up.html',{ 'form' : form })

