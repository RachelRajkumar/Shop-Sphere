from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Register
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


# Login
def user_login(request):

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")

    return render(request, "accounts/login.html", {"form": form})


# Logout
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


# Delete Account
@login_required
def delete_account(request):

    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect("register")

    return render(request, "accounts/delete_account.html")