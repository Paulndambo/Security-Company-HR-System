from django.shortcuts import render
from apps.payments.models import EmployeeSalary, EmployeeOvertime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/users/login")
def employee_salaries(request):
    salaries = EmployeeSalary.objects.all().order_by("-created")

    paginator = Paginator(salaries, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, 'salaries/salaries.html', context)


def overtimes(request):
    overtimes = EmployeeOvertime.objects.all()

    paginator = Paginator(overtimes, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "salaries/overtimes.html", context)


def record_overtime(request):
    if request.method == "POST":
        pass