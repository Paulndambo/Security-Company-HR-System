from django.shortcuts import render, redirect
from apps.employees.models import Attendance
from django.core.paginator import Paginator
from apps.users.models import User
from datetime import datetime

date_today = datetime.now().date()
# Create your views here.
def attendaces(request):
    atteandaces = Attendance.objects.all().order_by('-created')

    paginator = Paginator(atteandaces, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, 'attendances/attendances.html', context)


def generate_attendance(request):
    employees = User.objects.filter(role="Employee")

    attendace_list = []

    for employee in employees:
        attendace_list.append(Attendance(
            employee=employee,
            date=date_today,
            checked_in=False
        ))

    Attendance.objects.bulk_create(attendace_list)
    return redirect("attendances")


def new_attendance(request):
    if request.method == 'POST':
        employee = request.POST.get('employee')

    return render(request, 'attendances/new_attendance.html')

def mark_absent(request, attendace_id):
    attendace = Attendance.objects.get(id=attendace_id)
    attendace.checked_in = False
    ac