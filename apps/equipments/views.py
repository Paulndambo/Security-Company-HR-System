from django.shortcuts import render, redirect
from apps.equipments.models import Equipment, EquipmentIssue
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/users/login")
def equipments(request):
    equipments = Equipment.objects.all().order_by("-created")

    paginator = Paginator(equipments, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "equipments/equipments.html", context)


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
    return render(request, "equipments/new_equipment.html")


@login_required(login_url="/users/login")
def edit_equipment(request):
    if request.method == "POST":
        equipment_id = request.POST.get("equipment")
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        category = request.POST.get("category")

        equipment = Equipment.objects.get(id=equipment_id)
        equipment.quantity = quantity
        equipment.category = category
        equipment.price = price
        equipment.name = name
        equipment.save()

        return redirect("equipments")
    return render(request, "equipments/edit_equipment.html")


@login_required(login_url="/users/login")
def delete_equipment(request):
    if request.method == "POST":
        equipment_id = request.POST.get("equipment")
        equipment = Equipment.objects.get(id=equipment_id)
        equipment.delete()

        return redirect("equipments")

    return render(request, "equipments/delete_equipment.html")


@login_required(login_url="/users/login")
def issued_equipment(request):
    issued_equipment = EquipmentIssue.objects.all().order_by("-created")

    paginator = Paginator(issued_equipment, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "equipments/issued_equipment.html", context)


@login_required(login_url="/users/login")
def issue_equipment(request):
    user = request.user
    if request.method == "POST":
        employee = request.POST.get("employee")
        equipment = request.POST.get("equipment")
        quantity = request.POST.get("quantity")
        return_date = request.POST.get("return_date")

        EquipmentIssue.objects.create(
            employee_id=employee,
            equipment_id=equipment,
            quantity=quantity,
            return_date=return_date,
            issued_by=user,
            status="Pending Return",
        )

        return redirect("issued-equipments")
    return render(request, "equipments/issue_equipment.html")
