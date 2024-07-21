from django.shortcuts import render, redirect
from apps.payments.models import (
    EmployeeSalary,
    EmployeeOvertime,
    Payslip,
    BankInformation,
)
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
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "salaries/salaries.html", context)


def overtimes(request):
    overtimes = EmployeeOvertime.objects.all()
    employees = User.objects.filter(is_superuser=False)

    paginator = Paginator(overtimes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "employees": employees}
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
            amount=employee.job_category.overtime,
        )

        # Update Salary
        salary = EmployeeSalary.objects.filter(
            employee=employee, year=current_year, month=current_month
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
                overtime=employee.job_category.overtime,
            )

        return redirect("overtimes")

    return render(request, "salaries/record_overtime.html")


def payslips(request):
    payslips = Payslip.objects.all()

    paginator = Paginator(payslips, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

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
        action_type = request.POST.get("action_type")

        if action_type.lower() == "delete":
            payslips = Payslip.objects.filter(month=month_name, year=year)
            print(payslips)
        elif action_type.lower() == "generate":
            salaries = EmployeeSalary.objects.filter(month=month_name, year=year)
            salaries_list = []
            for salary in salaries:
                salaries_list.append(
                    Payslip(
                        employee=salary.employee,
                        month=salary.month,
                        year=salary.year,
                        days_worked=salary.days_worked,
                        daily_rate=salary.daily_rate,
                        overtime=salary.overtime,
                        total_amount=salary.total_amount,
                    )
                )

            Payslip.objects.bulk_create(salaries_list)
            # print(salaries_list)

        return redirect("payslips")
    return render(request, "salaries/generate_payslips.html")


def payslip_receipt(request, id):
    payslip = Payslip.objects.get(id=id)

    return render(request, "salaries/payslip_receipt.html", {"payslip": payslip})


# Service Provider Payment Details


def new_bank_details(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        bank_name = request.POST.get("bank_name")
        branch_name = request.POST.get("branch_name")
        account_name = request.POST.get("account_name")
        account_type = request.POST.get("account_type")
        account_number = request.POST.get("account_number")

        BankInformation.objects.create(
            employee_id=employee_id,
            bank_name=bank_name,
            branch_name=branch_name,
            account_name=account_name,
            account_type=account_type,
            account_number=account_number,
        )

        return redirect(f"/users/{employee_id}")
    return render(request, "bank/new_bank_details.html")


def edit_bank_details(request):
    if request.method == "POST":
        banking_info_id = request.POST.get("banking_info_id")
        employee_id = request.POST.get("employee_id")
        bank_name = request.POST.get("bank_name")
        branch_name = request.POST.get("branch_name")
        account_name = request.POST.get("account_name")
        account_type = request.POST.get("account_type")
        account_number = request.POST.get("account_number")

        banking_info = BankInformation.objects.get(id=banking_info_id)
        banking_info.account_number = account_number
        banking_info.account_type = account_type
        banking_info.account_name = account_name
        banking_info.bank_name = bank_name
        banking_info.branch_name = branch_name
        banking_info.save()

        return redirect(f"/users/{employee_id}")
    return render(request, "bank/edit_bank_details.html")
