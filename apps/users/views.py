from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from apps.users.models import User


from apps.core.models import Client, PaymentConfig, Workstation
from apps.employees.models import EmployeeDocument
from apps.payments.models import BankInformation


# Create your views here.
################ Authentication URLs ##############
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect("home")
    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
