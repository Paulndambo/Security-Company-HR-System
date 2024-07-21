from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from apps.visitors.models import Visitor, Visit


# Create your views here.
def visitors(request):
    visitors = Visitor.objects.all().order_by("-created")

    paginator = Paginator(visitors, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "visitors/visitors.html", context)


def new_visitor(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        id_number = request.POST.get("id_number")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        office_visiting = request.POST.get("office_visiting")
        visitation_reason = request.POST.get("visitation_reason")
        car_plate_number = request.POST.get("plate_number")
        car_model = request.POST.get("car_model")
        car_colour = request.POST.get("color")

        visitor = Visitor.objects.create(
            first_name=first_name,
            last_name=last_name,
            id_number=id_number,
            phone_number=phone_number,
            gender=gender,
            office_visiting=office_visiting,
            visitation_reason=visitation_reason,
            car_plate_number=car_plate_number,
            car_model=car_model,
            car_colour=car_colour,
        )

        return redirect("visitors")

    return render(request, "visitors/new_visitor.html")
