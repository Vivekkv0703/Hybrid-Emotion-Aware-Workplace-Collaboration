from .beans import EmployeeBean


class EmployeeBeanFactory:
    @staticmethod
    def from_model(employee):
        return EmployeeBean(
            id=str(employee.id),
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            role=employee.role,
            company_id=str(employee.company.id),
            is_active=employee.is_active,
            manager_id=str(employee.manager.id) if employee.manager else None,
            created_at=employee.created_at,
            updated_at=employee.updated_at,
        )
