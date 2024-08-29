from django.shortcuts import render, redirect
from apps.equipments.models import (
    Equipment,
    EquipmentIssue,
    Vehicle,
    VehicleFuelHistory,
    VehicleServiceHistory,
)
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.users.models import User
from django.db.models import Q
from apps.employees.models import Employee


# Create your views here.
@login_required(login_url="/users/login")
def equipments(request):
    equipments = Equipment.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")

        equipments = Equipment.objects.filter(Q(name__icontains=search_text))

    paginator = Paginator(equipments, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "operations/equipments/equipments.html", context)


@login_required(login_url="/users/login")
def new_equipment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        category = request.POST.get("category")

        Equipment.objects.create(
            name=name, price=price, quantity=quantity, category=category
        )

        return redirect("equipments")
    return render(request, "operations/equipments/new_equipment.html")


@login_required(login_url="/users/login")
def edit_equipment(request):
    if request.method == "POST":
        equipment_id = request.POST.get("equipment_id")
        equipment = Equipment.objects.get(id=equipment_id)

        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        category = request.POST.get("category")

        equipment.quantity = quantity
        equipment.category = category
        equipment.price = price
        equipment.name = name
        equipment.save()

        print(equipments)

        return redirect("equipments")
    return render(request, "operations/equipments/edit_equipment.html")


@login_required(login_url="/users/login")
def delete_equipment(request):
    if request.method == "POST":
        equipment_id = request.POST.get("equipment")
        equipment = Equipment.objects.get(id=equipment_id)
        equipment.delete()

        return redirect("equipments")

    return render(request, "operations/equipments/delete_equipment.html")


@login_required(login_url="/users/login")
def issued_equipment(request):
    issued_equipment = EquipmentIssue.objects.all().order_by("-created")

    employees = User.objects.filter(role="Employee")
    equipments = Equipment.objects.all()

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        issued_equipment = EquipmentIssue.objects.filter(
            Q(employee__first_name__icontains=search_text)
            | Q(employee__last_name__icontains=search_text)
            | Q(employee__id_number__icontains=search_text)
        )

    paginator = Paginator(issued_equipment, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "employees": employees, "equipments": equipments}

    return render(request, "operations/equipments/issued_equipment.html", context)


@login_required(login_url="/users/login")
def issue_equipment(request):
    user = request.user
    if request.method == "POST":
        employee = request.POST.get("employee")
        date_issued = request.POST.get("date_issued")

        head_cap_issued = request.POST.get("head_cap_issued")
        shirt_issued = request.POST.get("shirt_issued")
        belt_issued = request.POST.get("belt_issued")
        chest_guard_issued = request.POST.get("chest_guard_issued")
        shoes_issued = request.POST.get("shoes_issued")
        boots_issued = request.POST.get("boots_issued")
        sweater_issued = request.POST.get("sweater_issued")
        baton_issued = request.POST.get("baton_issued")
        trouser_issued = request.POST.get("trouser_issued")

        EquipmentIssue.objects.create(
            employee_id=employee,
            date_issued=date_issued,
            issued_by=user,
            baton_issued=True if baton_issued else False,
            sweater_issued=True if sweater_issued else False,
            boots_issued=True if boots_issued else False,
            shoes_issued=True if shoes_issued else False,
            chest_guard_issued=True if chest_guard_issued else False,
            belt_issued=True if belt_issued else False,
            shirt_issued=True if shirt_issued else False,
            head_cap_issued=True if head_cap_issued else False,
            trouser_issued=True if trouser_issued else False,
        )

        return redirect("issued-equipments")
    return render(request, "operations/equipments/issue_equipment.html")


@login_required(login_url="/users/login")
def mark_issued_equipment(request):
    if request.method == "POST":
        equipment_issue_id = request.POST.get("issue_id")
        action_type = request.POST.get("action_type")

        issued_equipment = EquipmentIssue.objects.get(id=equipment_issue_id)
        issued_equipment.status = action_type
        issued_equipment.save()

        return redirect("issued-equipments")
    return render(request, "operations/equipments/mark.html")


@login_required(login_url="/users/login")
def delete_issued_equipment(request):
    if request.method == "POST":
        equipment_issue_id = request.POST.get("issue_id")

        issued_equipment = EquipmentIssue.objects.get(id=equipment_issue_id)
        issued_equipment.delete()

        return redirect("issued-equipments")
    return render(request, "operations/equipments/delete_issue.html")


## Vehicles Management
@login_required(login_url="/users/login")
def vehicles(request):
    vehicles = Vehicle.objects.all().order_by("-created")
    employees = Employee.objects.all()
    if request.method == "POST":
        search_text = request.POST.get("search_text")
        vehicles = Vehicle.objects.filter(
            Q(plate_number__icontains=search_text)
            | Q(vehicle_model__icontains=search_text)
            | Q(vehicle_type__icontains=search_text)
        )

    paginator = Paginator(vehicles, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "employees": employees}
    return render(request, "operations/vehicles/vehicles.html", context)

@login_required(login_url="/users/login")
def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(id=id)

    # Fueling records
    fuel_records = vehicle.fuelingrecords.all().order_by("-created")
    fuel_paginator = Paginator(fuel_records, 5)
    fuel_page_number = request.GET.get("fuel_page")
    fuel_page_obj = fuel_paginator.get_page(fuel_page_number)

    # Fueling records
    service_records = vehicle.servicerecords.all().order_by("-created")
    service_paginator = Paginator(service_records, 5)
    service_page_number = request.GET.get("service_page")
    service_page_obj = service_paginator.get_page(service_page_number)
    
    context = {
        "vehicle": vehicle,
        "fuel_page_obj": fuel_page_obj,
        "service_page_obj": service_page_obj
    }
    return render(request, "operations/vehicles/vehicle_details.html", context)


@login_required(login_url="/users/login")
def new_vehicle(request):
    if request.method == "POST":
        vehicle_model = request.POST.get("vehicle_model")
        plate_number = request.POST.get("plate_number")
        vehicle_type = request.POST.get("vehicle_type")

        vehicle_status = request.POST.get("vehicle_status")

        Vehicle.objects.create(
            vehicle_model=vehicle_model,
            plate_number=plate_number,
            vehicle_type=vehicle_type,
            vehicle_status=vehicle_status
        )
        return redirect("vehicles")
    return render(request, "operations/vehicles/new_vehicle.html")


@login_required(login_url="/users/login")
def edit_vehicle(request):
    if request.method == "POST":
        vehicle_id = request.POST.get("vehicle_id")
        vehicle_model = request.POST.get("vehicle_model")
        plate_number = request.POST.get("plate_number")
        vehicle_type = request.POST.get("vehicle_type")
        vehicle_status = request.POST.get("vehicle_status")

        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.vehicle_model = vehicle_model
        vehicle.plate_number = plate_number
        vehicle.vehicle_type = vehicle_type
        vehicle.vehicle_status = vehicle_status
        vehicle.save()

        return redirect("vehicles")
    return render(request, "operations/vehicles/edit_vehicle.html")


@login_required(login_url="/users/login")
def delete_vehicle(request):
    if request.method == "POST":
        vehicle_id = request.POST.get("vehicle_id")
        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.delete()
        return redirect("vehicles")
    return render(request, "operations/vehicles/delete_vehicle.html")


@login_required(login_url="/users/login")
def assign_vehicle(request):
    if request.method == "POST":
        vehicle_id = request.POST.get("vehicle")
        employee = request.POST.get("employee")

        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.assigned_to_id = employee
        vehicle.save()

        return redirect("vehicles")
    return render(request, "operations/vehicles/assign_vehicle.html")


@login_required(login_url="/users/login")
def vehicle_fueling_history(request, id):
    fueling_history = VehicleFuelHistory.objects.filter(vehicle_id=id).order_by("-created")
    paginator = Paginator(fueling_history, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "operations/vehicles/fuel_history.html", context)


@login_required(login_url="/users/login")
def new_fuel_record(request):
    if request.method == "POST":
        vehicle = request.POST.get("vehicle")
        fueled_at = request.POST.get("fueled_at")
        amount = request.POST.get("amount")
        cost = request.POST.get("cost")
        date_fueled = request.POST.get("date_fueled")

        VehicleFuelHistory.objects.create(
            vehicle_id=vehicle,
            fueled_at=fueled_at,
            amount=amount,
            cost=cost,
            date_fueled=date_fueled
        )
        return redirect(f"/equipments/vehicles/{vehicle}")
    return render(request, "operations/fuel/record_fuel.html")


@login_required(login_url="/users/login")
def vehicle_service_history(request, id):
    service_history = VehicleServiceHistory.objects.filter(vehicle_id=id).order_by("-created")
    paginator = Paginator(service_history, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "vehicles/service_history.html", context)

@login_required(login_url="/users/login")
def new_repair_record(request):
    if request.method == "POST":
        vehicle = request.POST.get("vehicle")
        cost = request.POST.get("cost")
        date_serviced = request.POST.get("date_serviced")
        serviced_at = request.POST.get("serviced_at")

        VehicleServiceHistory.objects.create(
            vehicle_id=vehicle,
            cost=cost,
            date_serviced=date_serviced,
            serviced_at=serviced_at
        )
        return redirect(f"/equipments/vehicles/{vehicle}")
    return render(request, "operations/repair/record_repair.html")

