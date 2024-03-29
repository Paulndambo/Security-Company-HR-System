from django.shortcuts import render, redirect
from apps.core.models import Workstation
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, "home.html")


def workstations(request):
    work_stations = Workstation.objects.all().order_by('-created')

    paginator = Paginator(work_stations, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "workstations/work_stations.html", context)


def new_workstation(request):
    if request.method == 'POST':
        name  = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        contract_start_date = request.POST.get('contract_start_date')
        guards_posted = request.POST.get('guards_posted')
        guards_needed = request.POST.get('guards_needed')
        work_shift = request.POST.get('work_shift')
        location_description = request.POST.get('location_description')

        address = request.POST.get('address')
        town = request.POST.get('town')
        county = request.POST.get('county')
        country = request.POST.get('country')

        Workstation.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            contract_start_date=contract_start_date,
            guards_needed=guards_needed,
            guards_posted=guards_posted,
            work_shift=work_shift,
            location_description=location_description,
            postal_address=address,
            town=town,
            county=county,
            country=country,
        )

        return redirect("workstations")
    return render(request, 'workstations/new_workstation.html')


def edit_workstation(request):
    if request.method == 'POST':
        workstation_id = request.POST.get('workstation_id')
        name  = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        contract_start_date = request.POST.get('contract_start_date')
        guards_posted = request.POST.get('guards_posted')
        guards_needed = request.POST.get('guards_needed')
        work_shift = request.POST.get('work_shift')
        location_description = request.POST.get('location_description')

        address = request.POST.get('address')
        town = request.POST.get('town')
        county = request.POST.get('county')
        country = request.POST.get('country')

        workstation = Workstation.objects.get(id=workstation_id)
        workstation.name = name 
        workstation.phone_number = phone_number
        workstation.email = email
        workstation.contract_start_date = contract_start_date
        workstation.guards_needed = guards_needed
        workstation.guards_posted = guards_posted
        workstation.work_shift = work_shift
        workstation.location_description = location_description
        workstation.postal_address = address
        workstation.town=town
        workstation.county=county
        workstation.country=country
        workstation.save()

        return redirect("workstations")
    return render(request, 'workstations/edit_workstation.html')


def delete_workstation(request):
    if request.method == 'POST':
        workstation_id = request.POST.get('workstation_id')
        workstation = Workstation.objects.get(id=workstation_id)
        workstation.delete()
        return redirect("workstations")
    return render(request, 'workstations/delete_workstation.html')


def workstation_detail(request, workstation_id):
    workstation = Workstation.objects.get(id=workstation_id)

    context = {
        "workstation": workstation
    }
    return render(request, 'workstations/workstation_detail.html', context)