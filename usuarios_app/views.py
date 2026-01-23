from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from usuarios_app.forms import *

def register(request):

    if request.method == "POST":
        form = ClienteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_detail')
    else:
        form = ClienteCreateForm()
    
    return render(request, "usuarios_app/register.html", {"form": form})

@login_required   
def profile_detail(request):
    return render(request, "usuarios_app/profile_detail.html", {"user": request.user})

@login_required
def profile_change(request):
    if request.method == "POST":
        form = ClienteChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ClienteChangeForm(instance=request.user)

    return render(request, "usuarios_app/profile_edit.html", {"form":form})