from django.contrib import admin
from apps.core.models import Workstation, JobRole, PaymentConfig

# Register your models here.
admin.site.register(Workstation)
admin.site.register(JobRole)
admin.site.register(PaymentConfig)