from django.shortcuts import render, redirect
from apps.employees.models import Attendance, EmployeeLeave
from django.core.paginator import Paginator
from apps.users.models import User
from datetime import datetime
from django.db.models import Q

date_today = datetime.now().date()



# Create your views here.
def attendaces(request):
    atteandaces = Attendance.objects.all().order_by("-created")

    show_generate_attendance = False

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        atteandaces = Attendance.objects.filter(Q(employee__first_name__icontains=search_text) | Q(employee__last_name__icontains=search_text) | Q(employee__id_number__icontains=search_text))

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


def new_attendance(request):
    if request.method == "POST":
        employee = request.POST.get("employee")

    return render(request, "attendances/new_attendance.html")


def mark_attendance(request):
    if request.method == "POST":
        attendance_id = request.POST.get("attendance_id")
        action_type = request.POST.get("action_type")

        attendace = Attendance.objects.get(id=attendance_id)
        attendace.marked = True
        attendace.status = action_type
        attendace.save()

        return redirect("attendances")
    return render(request, "attendances/mark_attendance.html")

def reset_attendance(request, attendance_id):
    attendace = Attendance.objects.get(id=attendance_id)
    attendace.marked = False
    attendace.status = None
    attendace.save()

    return redirect("attendances")


def mark_present(request, attendance_id):
    user = request.user
    attendace = Attendance.objects.get(id=attendance_id)
    attendace.marked = True
    attendace.status = "Present"
    attendace.checked_in_by = user
    attendace.checkin_time = datetime.now()
    attendace.save()
    return redirect("attendances")


def mark_absent(request):
    user = request.user
    if request.method == "POST":
        attendance_id = request.POST.get("attendance_id")
        attendace = Attendance.objects.get(id=attendance_id)
        attendace.marked = True
        attendace.status = "Absent"
        attendace.checked_in_by = user
        attendace.checkin_time = datetime.now()
        attendace.save()
        return redirect("attendances")

    return render(request, "attendances/mark_absent.html")


# Employee Leave Management
def leave_applications(request):
    leave_applications = EmployeeLeave.objects.all().order_by("-created")

    paginator = Paginator(leave_applications, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    employees = User.objects.filter(role="Employee")

    context = {
        "page_obj": page_obj,
        "employees": employees
    }

    return render(request, "leaves/leaves.html", context)


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
            leave_to=leave_to
        )
        
        return redirect("leave-applications")
        
    return render(request, "leaves/apply_leave.html")