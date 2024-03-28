from django.shortcuts import render, redirect
from apps.employees.models import Attendance
from django.core.paginator import Paginator
from apps.users.models import User
from datetime import datetime

date_today = datetime.now().date()


# Create your views here.
def attendaces(request):
    atteandaces = Attendance.objects.all().order_by("-created")

    show_generate_attendance = False

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
