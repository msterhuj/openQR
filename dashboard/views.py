from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login

from .auth_forms import LoginForm


def index_view(request):
    if not request.user.is_authenticated:
        return redirect("dashboard_login")

    return render(request, "dashboard/index.html.j2")


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard_index")

    if request.method != "POST":
        return render(request, "dashboard/auth/login.html", {"form": LoginForm()})

    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, "dashboard/auth/login.html", {"form": form})

    username = form.cleaned_data["inputUsername"]
    password = form.cleaned_data["inputPassword"]
    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request, "dashboard/auth/login.html", {"form": form})

    login(request, user)

    return redirect("dashboard_index")


def register_view(request):
    return render(request, "dashboard/auth/register.html")


def logout_view(request):
    auth_logout(request)
    return redirect("front_index")
