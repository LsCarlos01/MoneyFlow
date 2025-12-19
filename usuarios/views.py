from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout





# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Já existe um usuário com esse username')
        return redirect('cadastro')

    User.objects.create_user(
        username=username,
        email=email,
        password=senha
    )

    messages.success(request, 'Cadastro realizado com sucesso')
    return redirect('login')


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')

    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user = authenticate(request, username=username, password=senha)

    if user is not None:
        auth_login(request, user)
        return redirect('dashboard')

    messages.error(request, 'Usuário ou senha inválidos')
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')