from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Todo


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('todo')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


loginn = login


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})
        user = User.objects.create_user(username=username, password=password)
        auth_login(request, user)
        return redirect('todo')
    return render(request, 'signup.html')


@login_required(login_url='login')
def todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        Todo.objects.create(user=request.user, title=task)
        return redirect('todo')
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'todos': todos})


@login_required(login_url='login')
def delete(request, pk):
    Todo.objects.filter(id=pk, user=request.user).delete()
    return redirect('todo')


# ✅ இதை மட்டும் புதுசா add பண்ணினோம்
@login_required(login_url='login')
def edit(request, id):
    todo = Todo.objects.filter(id=id, user=request.user).first()
    if not todo:
        return redirect('todo')
    if request.method == 'POST':
        task = request.POST.get('task', '').strip()
        if task:
            todo.title = task
            todo.save()
        return redirect('todo')
    return render(request, 'edit.html', {'todo': todo})


def logoutt(request):
    auth_logout(request)
    return redirect('login')