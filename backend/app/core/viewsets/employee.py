from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..domain.employee.employee_datastore import EmployeeDataStore


class Employee(ViewSet):
    def _bean_to_dict(self, employee_bean):
        return {
            "id": employee_bean.id,
            "first_name": employee_bean.first_name,
            "last_name": employee_bean.last_name,
            "email": employee_bean.email,
            "role": employee_bean.role,
            "is_active": employee_bean.is_active,
            "company_id": employee_bean.company_id,
            "manager_id": employee_bean.manager_id,
            "created_at": employee_bean.created_at,
            "updated_at": employee_bean.updated_at,
        }

    def list(self, request, company_id=None):
        if not company_id:
            return Response(
                {"error": "Company id is mandatory"}, status=HTTP_400_BAD_REQUEST
            )
        beans = EmployeeDataStore.list_employees(company_id)
        response_data = [self._bean_to_dict(bean) for bean in beans]
        return Response(response_data, status=HTTP_200_OK)

    def retrieve(self, request, company_id=None, pk=None):
        if not pk or not company_id:
            return Response(
                {"error": "Employee id and company id is mandatory"},
                status=HTTP_400_BAD_REQUEST,
            )
        bean = EmployeeDataStore.get_employee(pk)
        response_data = self._bean_to_dict(bean)
        return Response(response_data, status=HTTP_200_OK)

    def create(self, request, company_id=None):
        bean = EmployeeDataStore.create_employee(company_id, request.data)
        response_data = self._bean_to_dict(bean)
        return Response(response_data, status=HTTP_201_CREATED)

    def destroy(self, request, company_id=None, pk=None):
        EmployeeDataStore.delete_employee(pk)
        return Response(status=HTTP_204_NO_CONTENT)

    def update(self, request, company_id=None, pk=None):
        bean = EmployeeDataStore.update_employee(pk, request.data)
        response_data = self._bean_to_dict(bean)
        return Response(response_data, status=HTTP_200_OK)
