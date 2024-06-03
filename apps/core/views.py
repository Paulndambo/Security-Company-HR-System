from django.shortcuts import render, redirect
from apps.core.models import Workstation, Client, PaymentConfig
from apps.users.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login")
def home(request):
    employees_count = User.objects.all().count()
    clients_count = Client.objects.all().count()

    context = {
        "employees_count": employees_count,
        "clients_count": clients_count
    }
    return render(request, "home.html", context)


@login_required(login_url="/users/login")
def clients(request):
    work_stations = Client.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text") 
        work_stations = Client.objects.filter(Q(name__icontains=search_text))

    paginator = Paginator(work_stations, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "clients/clients.html", context)


@login_required(login_url="/users/login")
def new_client(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        contract_start_date = request.POST.get("contract_start_date")
        guards_posted = request.POST.get("guards_posted")
        guards_needed = request.POST.get("guards_needed")
        work_shift = request.POST.get("work_shift")
        location_description = request.POST.get("location_description")

        address = request.POST.get("address")
        town = request.POST.get("town")
        county = request.POST.get("county")
        country = request.POST.get("country")

        Client.objects.create(
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

        return redirect("clients")
    return render(request, "clients/new_client.html")

@login_required(login_url="/users/login")
def edit_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        contract_start_date = request.POST.get("contract_start_date")
        guards_posted = request.POST.get("guards_posted")
        guards_needed = request.POST.get("guards_needed")
        work_shift = request.POST.get("work_shift")
        location_description = request.POST.get("location_description")

        address = request.POST.get("address")
        town = request.POST.get("town")
        county = request.POST.get("county")
        country = request.POST.get("country")

        client = Client.objects.get(id=client_id)
        client.name = name
        client.phone_number = phone_number
        client.email = email
        client.contract_start_date = contract_start_date
        client.guards_needed = guards_needed
        client.guards_posted = guards_posted
        client.work_shift = work_shift
        client.location_description = location_description
        client.postal_address = address
        client.town = town
        client.county = county
        client.country = country
        client.save()

        return redirect("clients")
    return render(request, "clients/edit_client.html")

@login_required(login_url="/users/login")
def delete_client(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        client = Client.objects.get(id=client_id)
        client.delete()
        return redirect("clients")
    return render(request, "clients/delete_client.html")

@login_required(login_url="/users/login")
def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)

    guards = client.clientsguards.all()
    workstations = client.workstations.all()
    paginator = Paginator(guards, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"client": client, "page_obj": page_obj, "workstations": workstations}
    return render(request, "clients/client_detail.html", context)


## Work stations
def new_workstation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        client_id = request.POST.get("client_id")
        guards_needed = request.POST.get("guards_needed")
        guards_posted = request.POST.get("guards_posted")
        work_shift = request.POST.get("work_shift")

        Workstation.objects.create(
            name=name, 
            client_id=client_id, 
            guards_needed=guards_needed, 
            guards_posted=guards_posted,
            work_shift=work_shift
        )

        return redirect(f"/clients/{client_id}")
    return render(request, "workstations/new_workstation.html")


def edit_workstation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        client_id = request.POST.get("client_id")
        workstation_id = request.POST.get("workstation_id")
        guards_needed = request.POST.get("guards_needed")
        guards_posted = request.POST.get("guards_posted")
        work_shift = request.POST.get("work_shift")

        workstation = Workstation.objects.get(id=workstation_id)
        workstation.name = name
        workstation.guards_needed = guards_needed
        workstation.work_shift = work_shift
        workstation.guards_posted = guards_posted
        workstation.save()

        return redirect(f"/clients/{client_id}")
    return render(request, "workstations/edit_workstation.html")

def delete_workstation(request):
    if request.method == "POST":
        workstation_id = request.POST.get('workstation_id')
        client_id = request.POST.get('client_id')
        workstation = Workstation.objects.get(id=workstation_id)
        workstation.delete()
        return redirect(f"/clients/{client_id}")
    return render(request, "workstations/delete_workstation.html")


def payments(request):
    payments = PaymentConfig.objects.all()
    context = {
        "payments": payments
    }

    return render(request, "salaries/payments.html", context)


def new_payment_config(request):
    if request.method == "POST":
        job_group = request.POST.get("job_group")
        overtime = request.POST.get("overtime")
        daily_rate = request.POST.get("daily_rate")

        PaymentConfig.objects.create(
            job_group=job_group,
            overtime=overtime,
            daily_rate=daily_rate
        )

        return redirect("payment-configs")
    return render(request, "salaries/new_payment_config.html")


def edit_payment_config(request):
    if request.method == "POST":
        payment_id = request.POST.get("payment_id")
        job_group = request.POST.get("job_group")
        overtime = request.POST.get("overtime")
        daily_rate = request.POST.get("daily_rate")

        payment_config = PaymentConfig.objects.get(id=payment_id)
        payment_config.job_group = job_group
        payment_config.overtime = overtime
        payment_config.daily_rate = daily_rate
        payment_config.save()

        return redirect("payment-configs")
    return render(request, "salaries/edit_payment_config.html")

def delete_payment_config(request):
    if request.method == "POST":
        payment_id = request.POST.get("payment_id")
        payment_config = PaymentConfig.objects.get(id=payment_id)
        payment_config.delete()

        return redirect("payment-configs")
    return render(request, "salaries/delete_payment_config.html")


