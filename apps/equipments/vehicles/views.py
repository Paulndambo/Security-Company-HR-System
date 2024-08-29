from django.shortcuts import render, redirect
from apps.equipments.models import (
    VehicleFuelHistory,
    VehicleServiceHistory,
)
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.users.models import User
from django.db.models import Q

@login_required(login_url="/users/login")
def new_fueling_record(request):
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
        return redirect("fueling-history")
    return render(request, "operations/operations/fuel/new_record_fuel.html")


@login_required(login_url="/users/login")
def new_service_record(request):
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
        return redirect("servicing-history")
    return render(request, "operations/repair/new_service_record.html")