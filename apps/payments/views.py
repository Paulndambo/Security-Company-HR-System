from django.shortcuts import render
from apps.payments.models import EmployeeSalary
from django.core.paginator import Paginator
# Create your views here.
def employee_salaries(request):
    salaries = EmployeeSalary.objects.all().order_by("-created")

    paginator = Paginator(salaries, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, 'salaries/salaries.html', context)
