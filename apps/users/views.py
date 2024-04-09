from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from apps.users.models import User

from apps.core.models import Workstation

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


@login_required(login_url="/users/login/")
def employees(request):
    employees = User.objects.all().order_by("-created")
    workstations = Workstation.objects.all()

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        employees = User.objects.filter(
            Q(first_name__icontains=search_text)
            | Q(first_name__icontains=search_text)
            | Q(phone_number__icontains=search_text)
            | Q(id_number__icontains=search_text)
        ).order_by("-created")

    paginator = Paginator(employees, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "workstations": workstations}
    return render(request, "employees/employees.html", context)


@login_required(login_url="/users/login/")
def new_employee(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        id_number = request.POST.get("id_number")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        physical_address = request.POST.get("address")
        postal_address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        county = request.POST.get("county")
        position = request.POST.get("position")
        nhif_number = request.POST.get("nhif_number")
        nssf_number = request.POST.get("nssf_number")

        chief_letter = request.FILES.get("chief_letter")
        police_clearance = request.FILES.get("police_clearance")
        recommendation_letter = request.FILES.get("recommendation_letter")
        scanned_id = request.FILES.get("scanned_id")
        passport_photo = request.FILES.get("passport_photo")
        #workstation = request.POST.get("workstation")

        employee = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=id_number,
            gender=gender,
            id_number=id_number,
            phone_number=phone_number,
            email=email,
            physical_address=physical_address,
            postal_address=postal_address,
            town=city,
            county=county,
            country=country,
            position=position,
            nhif_number=nhif_number,
            nssf_number=nssf_number,
            role="Employee",
            #workstation_id=workstation,
            chief_letter=chief_letter,
            police_clearance=police_clearance,
            recommendation_letter=recommendation_letter,
            scanned_id=scanned_id,
            passport_photo=passport_photo,
        )

        return redirect("employees")
    return render(request, "employees/new_employees.html")


@login_required(login_url="/users/login/")
def edit_employee(request):
    if request.method == "POST":
        workstation = request.POST.get("workstation")
        employee_id = request.POST.get("employee_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        position = request.POST.get("position")
        gender = request.POST.get("gender")
        id_number = request.POST.get("id_number")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        county = request.POST.get("county")
        country = request.POST.get("country")
        nhif_number = request.POST.get("nhif_number")
        nssf_number = request.POST.get("nssf_number")

        employee = User.objects.get(id=employee_id)
        employee.first_name = first_name
        employee.last_name = last_name
        employee.gender = gender
        employee.id_number = id_number
        employee.email = email
        employee.phone_number = phone_number
        employee.physical_address = address
        employee.postal_address = address
        employee.town = city
        employee.position = position
        employee.county = county
        employee.country = country
        employee.nhif_number = nhif_number
        employee.nssf_number = nssf_number
        employee.workstation_id = workstation
        employee.save()

        return redirect("employees")

    return render(request, "employees/edit_employee.html")


@login_required(login_url="/users/login/")
def delete_employee(request):
    if request.method == "POST":
        
        employee_id = request.POST.get("employee_id")
        employee = User.objects.get(id=employee_id)
        employee.delete()

        return redirect("employees")

    return render(request, "employees/delete_employee.html")


@login_required(login_url="/users/login/")
def employee_details(request, employee_id=None):
    employee = User.objects.get(id=employee_id)
    family_members = employee.nextofkins.all()
    education_details = employee.educationdetails.all()

    context = {
        "employee": employee,
        "family_members": family_members,
        "education_details": education_details
    }

    return render(request, "employees/employee_details.html", context)
