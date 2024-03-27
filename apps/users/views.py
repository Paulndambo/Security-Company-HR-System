from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from apps.users.models import User

# Create your views here.
# Create your views here.
################ Authentication URLs ##############
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('home')
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/users/login/")
def employees(request):
    employees = User.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        employees = User.objects.filter(
            Q(first_name__icontains=search_text) | Q(first_name__icontains=search_text) | Q(phone_number__icontains=search_text) | Q(
                id_number__icontains=search_text)
        ).order_by("-created")

    paginator = Paginator(employees, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
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
            role="Employee"
        )

        return redirect("employees")
    return render(request, "employees/new_employees.html")


@login_required(login_url="/users/login/")
def edit_employee(request):
    if request.method == "POST":
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
        employee.save()

        return redirect("employees")

    return render(request, "employees/edit_employee.html")


@login_required(login_url="/users/login/")
def delete_employee(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee_id")
        employee = User.objects.get(id=employee_id)
        employee.delete()

        return redirect("members")

    return render(request, "employees/delete_employee.html")


@login_required(login_url="/users/login/")
def employee_details(request, employee_id=None):
    employee = User.objects.get(id=employee_id)

    context = {
        "employee": employee,
    }

    return render(request, "employees/employee_details.html", context)
