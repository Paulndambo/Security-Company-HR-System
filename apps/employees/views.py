from django.shortcuts import render, redirect
from apps.employees.models import Attendance, EmployeeLeave
from django.core.paginator import Paginator
from apps.users.models import User
from datetime import datetime
import calendar
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from apps.payments.models import EmployeeSalary
from apps.employees.models import NextOfKin, EducationInformation, BankInformation

date_today = datetime.now().date()

current_month = calendar.month_name[date_today.month]
current_year = str(date_today.year)
# Create your views here.
@login_required(login_url="/users/login")
def attendaces(request):
    atteandaces = Attendance.objects.all().order_by("-created")

    show_generate_attendance = False

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        atteandaces = Attendance.objects.filter(
            Q(employee__first_name__icontains=search_text)
            | Q(employee__last_name__icontains=search_text)
            | Q(employee__id_number__icontains=search_text)
        )

    employees = User.objects.filter(role="Employee")
    attendances_today = Attendance.objects.filter(date=date_today).count()

    if attendances_today < employees.count():
        show_generate_attendance = True

    paginator = Paginator(atteandaces, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "show_generate_attendance": show_generate_attendance,
    }
    return render(request, "attendances/attendances.html", context)


@login_required(login_url="/users/login")
def generate_attendance(request):
    employees = User.objects.filter(role="Employee")
    attendances_today = Attendance.objects.filter(date=date_today).count()

    print(f"The Attendance Today is: {attendances_today}")

    if employees.count() > attendances_today:
        attendace_list = []

        for employee in employees:
            attendace_list.append(
                Attendance(employee=employee, date=date_today, marked=False)
            )

        Attendance.objects.bulk_create(attendace_list)

    return redirect("attendances")


@login_required(login_url="/users/login")
def new_attendance(request):
    if request.method == "POST":
        employee = request.POST.get("employee")

    return render(request, "attendances/new_attendance.html")


@login_required(login_url="/users/login")
def mark_attendance(request):
    user = request.user
    if request.method == "POST":
        attendance_id = request.POST.get("attendance_id")
        action_type = request.POST.get("action_type")

        attendace = Attendance.objects.get(id=attendance_id)
        attendace.marked = True
        attendace.status = action_type
        attendace.checked_in_by = user
        attendace.checkin_time = datetime.now()

        attendace.save()

        return redirect("attendances")
    return render(request, "attendances/mark_attendance.html")


@login_required(login_url="/users/login")
def reset_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    current_status = attendance.status
    attendance.marked = False
    attendance.status = None
    attendance.save()

    ## Update Salary
    if current_status == "Present":
        salary = EmployeeSalary.objects.filter(employee=attendance.employee).first()

        if salary:
            salary.total_amount -= salary.daily_rate
            salary.days_worked -= 1
            salary.save()

    return redirect("attendances")


@login_required(login_url="/users/login")
def mark_present(request, attendance_id):
    user = request.user
    attendace = Attendance.objects.get(id=attendance_id)
    attendace.marked = True
    attendace.status = "Present"
    attendace.checked_in_by = user
    attendace.checkin_time = datetime.now()
    attendace.save()

    # Update Salary
    salary = EmployeeSalary.objects.filter(
        employee=attendace.employee, 
        year=current_year,
        month=current_month
    ).first()

    if salary:
        salary.total_amount += user.daily_rate
        salary.days_worked += 1
        salary.save()
    else:
        salary = EmployeeSalary.objects.create(
            employee=attendace.employee,
            month=current_month,
            year=current_year,
            days_worked=1,
            daily_rate=user.daily_rate,
            total_amount=user.daily_rate
        )

    return redirect("attendances")


@login_required(login_url="/users/login")
def mark_absent(request, attendance_id):
    user = request.user
    attendace = Attendance.objects.get(id=attendance_id)
    attendace.marked = True
    attendace.status = "Absent"
    attendace.checked_in_by = user
    attendace.checkin_time = datetime.now()
    attendace.save()
    return redirect("attendances")



# Employee Leave Management
@login_required(login_url="/users/login")
def leave_applications(request):
    leave_applications = EmployeeLeave.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")

        leave_applications = EmployeeLeave.objects.filter(Q(employee__first_name__icontains=search_text) | Q(employee__last_name__icontains=search_text))

    paginator = Paginator(leave_applications, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    employees = User.objects.filter(role="Employee")

    context = {"page_obj": page_obj, "employees": employees}

    return render(request, "leaves/leaves.html", context)


@login_required(login_url="/users/login")
def apply_leave(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        days_applied = request.POST.get("days_applied")
        leave_type = request.POST.get("leave_type")
        leave_from = request.POST.get("leave_from")
        leave_to = request.POST.get("leave_to")

        EmployeeLeave.objects.create(
            employee_id=employee_id,
            days_applied=days_applied,
            leave_type=leave_type,
            leave_from=leave_from,
            leave_to=leave_to,
        )

        return redirect("leave-applications")

    return render(request, "leaves/apply_leave.html")


@login_required(login_url="/users/login")
def mark_leave_application(request):
    if request.method == "POST":
        leave_id = request.POST.get("leave_id")
        action_type = request.POST.get("action_type")

        leave = EmployeeLeave.objects.get(id=leave_id)
        leave.status = action_type
        leave.save()

        return redirect("leave-applications")
    return render(request, "leaves/mark_leave.html")


@login_required(login_url="/users/login")
def delete_leave_application(request):
    if request.method == "POST":
        leave_id = request.POST.get("leave_id")
        leave = EmployeeLeave.objects.get(id=leave_id)
        leave.delete()
        return redirect("leave-applications")
    return render(request, "leaves/delete_leave.html")


### NEXT OF KIN RECORDS MANAGEMENT
def new_relative(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        relationship = request.POST.get("relationship")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")

        relative = NextOfKin.objects.create(
            employee_id=employee_id, 
            first_name=first_name, 
            last_name=last_name, 
            gender=gender, 
            relation=relationship,
            email=email,
            phone_number=phone_number
        )
        

        return redirect(f"/users/{employee_id}")
    return render(request, "family/new_family_member.html")



def edit_relative(request):
    if request.method == "POST":
        family_member_id = request.POST.get("family_member_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        relationship = request.POST.get("relationship")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")

        relative = NextOfKin.objects.get(id=family_member_id)
        relative.first_name=first_name
        relative.last_name=last_name
        relative.gender=gender
        relative.relation=relationship
        relative.email=email
        relative.phone_number=phone_number
        relative.save()

        return redirect(f"/users/{relative.employee.id}")
    return render(request, "family/edit_relative.html")


def delete_relative(request):
    if request.method == "POST":
        relative_id = request.POST.get("relative_id")
        relative = NextOfKin.objects.get(id=relative_id)
        employee_id = relative.employee.id
        relative.delete()
        return redirect(f"/users/{employee_id}")
    
    return render(request, "family/delete_relative.html")


## EDUCATION RECORDS MANAGEMENT

def new_education_record(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        school_name = request.POST.get("school_name")
        level = request.POST.get("level")
        start_year = request.POST.get("start_year")
        graduation_year = request.POST.get("graduation_year")

        EducationInformation.objects.create(
            employee_id=employee_id,
            school_name=school_name,
            level=level,
            start_year=start_year,
            graduation_year=graduation_year
        )

        return redirect(f"/users/{employee_id}")
    return render(request, "education/new_education.html")


def edit_education_record(request):
    if request.method == "POST":
        education_id = request.POST.get("education_id")
        school_name = request.POST.get("school_name")
        level = request.POST.get("level")
        start_year = request.POST.get("start_year")
        graduation_year = request.POST.get("graduation_year")

        education = EducationInformation.objects.get(id=education_id)
        education.school_name=school_name
        education.level=level
        education.start_year=start_year
        education.graduation_year=graduation_year
        education.save()
        
        return redirect(f"/users/{education.employee.id}")
    return render(request, "education/edit_education.html")

def delete_education_record(request):
    if request.method == "POST":
        education_id = request.POST.get("education_id")
        employee_id = request.POST.get("employee_id")
        education = EducationInformation.objects.get(id=education_id)
        education.delete()

        return redirect(f"/users/{employee_id}")
    return render(request, "education/delete_education.html")


def new_bank_details(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        bank_name = request.POST.get('bank_name')
        branch_name = request.POST.get('branch_name')
        account_name = request.POST.get('account_name')
        account_type = request.POST.get('account_type')
        account_number = request.POST.get('account_number')

        BankInformation.objects.create(
            employee_id=employee_id,
            bank_name=bank_name,
            branch_name=branch_name,
            account_name=account_name,
            account_type=account_type,
            account_number=account_number
        )

        return redirect(f"/users/{employee_id}")
    return render(request, 'bank/new_bank_details.html')


def edit_bank_details(request):
    if request.method == 'POST':
        banking_info_id = request.POST.get('banking_info_id')
        employee_id = request.POST.get('employee_id')
        bank_name = request.POST.get('bank_name')
        branch_name = request.POST.get('branch_name')
        account_name = request.POST.get('account_name')
        account_type = request.POST.get('account_type')
        account_number = request.POST.get('account_number')

        banking_info = BankInformation.objects.get(id=banking_info_id)
        banking_info.account_number = account_number
        banking_info.account_type = account_type
        banking_info.account_name = account_name
        banking_info.bank_name = bank_name
        banking_info.branch_name = branch_name
        banking_info.save()

        return redirect(f"/users/{employee_id}")
    return render(request, 'bank/edit_bank_details.html')