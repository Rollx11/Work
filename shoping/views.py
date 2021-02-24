from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm, SearchForm
from .models import Drink




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'shoping/register.html', {'form': form})




def main(request):
    return render(request, 'shoping/main.html',)


def drinks(request):
    drinks = Drink.objects.all()

    return render(request, 'shoping/drinks.html', {'title': 'Главная страница сайта', 'drinks': drinks})


def about(request):
    return render(request, 'shoping/about.html',)


def logout_view(request):
    logout(request)

    return redirect('/')


def logins(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if request.GET and 'next' in request.GET:
                     return redirect(request.GET['next'])
                return redirect('/')
            else:
                form.add_error('login', 'Bad login or password')
                form.add_error('password', 'Bad login or password')
                return render(request, 'shoping/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'shoping/login.html', {'form':form})



