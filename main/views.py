from django.shortcuts import render, HttpResponseRedirect
from .models import problem
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            new_problem = problem()
            new_problem.whose_problem = user.username
            new_problem.title = request.POST.get("title")
            new_problem.description = request.POST.get("description")
            new_problem.deadline = request.POST.get("deadline")
            if new_problem.title and new_problem.description and new_problem.deadline:
                new_problem.save()
            else:
                return render(request, "warning.html")
        tasks = problem.objects.filter(whose_problem=user.username)
        return render(request, "main.html", {"tasks": tasks})
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "warning.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {
                "message": "Logged Out"
            })

