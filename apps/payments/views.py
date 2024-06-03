from django.shortcuts import render, redirect
from apps.payments.models import EmployeeSalary, EmployeeOvertime, Payslip
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from apps.users.models import User
import calendar

date_today = datetime.now().date()
current_month = calendar.month_name[date_today.month]
current_year = str(date_today.year)

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

        # Update Salary
        salary = EmployeeSalary.objects.filter(
            employee=employee, 
            year=current_year,
            month=current_month
        ).first()

        if salary:
            salary.total_amount += employee.job_category.overtime
            salary.overtime += employee.job_category.overtime
            salary.save()
        else:
            salary = EmployeeSalary.objects.create(
                employee=employee,
                month=current_month,
                year=current_year,
                days_worked=1,
                daily_rate=employee.job_category.daily_rate,
                total_amount=employee.job_category.daily_rate,
                overtime=employee.job_category.overtime
            )


        return redirect("overtimes")
    
    return render(request, "salaries/record_overtime.html")


def payslips(request):
    payslips = Payslip.objects.all()

    paginator = Paginator(payslips, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "salaries/payslips.html", context)


def delete_payslip(request):
    if request.method == "POST":
        payslip_id = request.POST.get("payslip_id")
        payslip = Payslip.objects.get(id=payslip_id)
        payslip.delete()

        return redirect("payslips")
    return redirect(request, "salaries/delete_payslip.html")

def generate_payslips(request):
    if request.method == "POST":
        month_name = request.POST.get("month")
        year = request.POST.get("year")

        salaries = EmployeeSalary.objects.filter(month=month_name, year=year)
        print(salaries)

        return redirect("payslips")
    return render(request, "salaries/generate_payslips.html")