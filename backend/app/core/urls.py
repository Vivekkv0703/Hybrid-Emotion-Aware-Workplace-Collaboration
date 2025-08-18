from django.urls import path
from .viewsets.employee import Employee

employee_list = Employee.as_view({"get": "list", "post": "create"})
employee_detail = Employee.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

urlpatterns = [
    path("companies/<str:company_id>/employees/", employee_list, name="employee-list"),
    path(
        "companies/<str:company_id>/employees/<str:pk>/",
        employee_detail,
        name="employee-detail",
    ),
]
