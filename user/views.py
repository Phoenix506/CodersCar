from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                newUser = User(username=username)
                newUser.set_password(password)
                newUser.save()
                login(request, newUser)
                messages.success(request, f'Qeydiyyat uğurla tamamlandı')
                return redirect('index')
            context = {'forms': form}
            return render(request, 'register.html', context)
        else:
            form = forms.RegisterForm()
            context = {'forms': form}
            return render(request, 'register.html', context)
    else:
        return redirect("index")


def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context = {'forms': form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        u = authenticate(username=username, password=password)
        if u is None:
            messages.warning(request, 'Ad və ya şifrə xətalıdır')
            return render(request, 'login.html', context)
        else:
            messages.success(request, 'Xoş Gəldiniz')
            login(request, u)
            return redirect('index')
    else:
        return render(request, 'login.html', context)

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'Çıxış oldunuz')
    return redirect('index')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Məlumatlarınız yeniləndi')
            return redirect('index')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'profile.html', context)
