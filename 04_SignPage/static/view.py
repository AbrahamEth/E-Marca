from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def choose_role(request):
    return render(request, "choose_role.html")

def admin_auth(request):
    return render(request, "admin_auth_code.html")

def verify_admin(request):
    if request.method == "POST":
        if request.POST.get("admin_code") == "ADMIN123":
            return redirect("/login/")
        return render(request, "admin_auth_code.html", {"error": "Invalid Code"})
    return redirect("/")

def login_user(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect("/admin-dashboard/")
        return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")
