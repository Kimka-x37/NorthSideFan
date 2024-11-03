from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main/main.html', {'username': request.user.username})

def admins(request):
    return render(request, 'main/admins.html', {'username': request.user.username})

def register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            auth.login(request, user)
            return redirect('main')
        else:
            form = Register_form()
            return render(request, 'main/register.html', {'form':form, 
                                                          'error':'Сталася помилка в реєстрації, можливо таке імя вже існує, спробуйте ще раз'})
    else:
        form = Register_form()
        return render(request, 'main/register.html', {'form':form, 'error':''})

def login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = request.POST['username'].lower()
            password = request.POST['password']

            user = authenticate(request, 
                                 username=username,
                                 password=password)

            if user is None:
                return render(request, 'main/login.html', {'form': form, 'error':'Можливо, ви щось неправильно ввели'})
            else:
                auth.login(request, user)
                return redirect('main')
        else:
            return render(request, 'main/login.html', {'form': form, 'error':'Можливо, ви щось неправильно ввели'})
    else:
        form = Login_form()
        return render(request, 'main/login.html', {'form': form, 'error':''})
    
@login_required(login_url='register')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main')
    else:
        return render(request, 'main/logout.html')