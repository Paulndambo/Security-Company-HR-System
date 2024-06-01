from django.shortcuts import render, redirect
from apps.payments.models import EmployeeSalary, EmployeeOvertime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from apps.users.models import User
import calendar
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
    employees = User.objects.all()

    paginator = Paginator(overtimes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "employees": employees
    }
    return render(request, "salaries/overtimes.html", context)


def record_overtime(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        date_str = request.POST.get("overtime_date")

        employee = User.objects.get(id=employee_id)

        overtime_date = datetime.strptime(date_str, "%Y-%m-%d")
        month_name = calendar.month_name[overtime_date.month]

        EmployeeOvertime.objects.create(
            employee=employee,
            overtime_date=date_str,
            month=month_name,
            year=str(overtime_date.year),
            amount=employee.job_category.overtime
        )

        return redirect("overtimes")
    
    return render(request, "salaries/record_overtime.html")
