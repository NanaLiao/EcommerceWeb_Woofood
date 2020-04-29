from django.shortcuts import render,redirect
from accounts.forms import (
        RegistrationForm,
        EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    return render(request,'account/home.html')


def register(request):

    if request.method =='POST':
        form  = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('items:home')
        else:
            messages.info(request, "Please confirm the password.")
            return redirect('/account/register')

    else:
        form = RegistrationForm()
        context={'form':form}
        return render(request,'account/reg_form.html',context)



@login_required
def view_profile(request):
    args ={'user':request.user}
    return render(request,'account/profile.html',args)

@login_required
def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'account/edit_profile.html',args)
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            messages.info(request, "Please check the error.")

            return redirect('/account/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'account/change_password.html',args)

#about {% if user.is_authenticated %} or  {% if request.user.is_authenticated %}  in base.html, the request object is being included in your view’s context. This request object contains a user object, which will have is_authenticated
#if the user is logged in.
