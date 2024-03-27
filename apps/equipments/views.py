from django.shortcuts import render, redirect
from apps.equipments.models import Equipment, EquipmentIssue
from django.core.paginator import Paginator
# Create your views here.
def equipments(request):
    equipments = Equipment.objects.all().order_by("-created")

    paginator = Paginator(equipments, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "equipments/equipments.html", context)


def new_equipment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        Equipment.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            category=category
        )

        return redirect("equipments")
    return render(request, 'equipments/new_equipment.html')


def issued_equipment(request):
    issued_equipment = EquipmentIssue.objects.all().order_by("-created")

    paginator = Paginator(issued_equipment, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "equipments/issued_equipment.html", context)
