from django.urls import path
from apps.visitors.views import visitors, new_visitor

urlpatterns = [
    path("", visitors, name="visitors"),
    path("new-visitor/", new_visitor, name="new-visitor"),
]