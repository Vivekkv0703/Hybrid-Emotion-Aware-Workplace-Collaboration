from rest_framework.test import APIClient
from .test_setup_mixin import TestSetupMixin
from ..models.company import Company
from ..models.employee import Employee
from ..utils.auth import create_access_token
from ..domain.employee.employee_datastore import EmployeeDataStore


class EmployeeTests(TestSetupMixin):
    def setUp(self):
        self.client = APIClient()

        # TODO: Use company datastore for creation of company model objects
        self.company = Company(
            name="test_company",
            domain="test.com",
            industry="finance",
            logo_url="example",
            location="America",
            state="New York",
        ).save()

    def tearDown(self):
        Company.objects.all().delete()
        Employee.objects.all().delete()

    def test_get_employee(self):
        data = {
            "first_name": "aryan",
            "last_name": "satija",
            "email": "aryan.satija@gmail.com",
            "password": "smile",
            "role": "software engineer",
            "manager": None,
            "is_active": True,
        }

        employee = EmployeeDataStore.create_employee(self.company.id, data)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(create_access_token(employee.id))}"
        )
        url = f"/api/core/companies/{self.company.id}/employees/{employee.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["first_name"], data["first_name"])
        self.assertEqual(response_data["last_name"], data["last_name"])
        self.assertEqual(response_data["email"], data["email"])
        self.assertIsNone(response_data["manager_id"])
        self.assertTrue(response_data["is_active"])

    def test_create_employee(self):
        data = {
            "first_name": "aryan",
            "last_name": "satija",
            "email": "aryan.satija@gmail.com",
            "password": "smile",
            "role": "software engineer",
            "manager": None,
            "is_active": True,
        }

        url = f"/api/core/companies/{self.company.id}/employees/"
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        self.assertEqual(response_data["employee"]["first_name"], data["first_name"])
        self.assertEqual(response_data["employee"]["last_name"], data["last_name"])
        self.assertEqual(response_data["employee"]["email"], data["email"])
        self.assertIsNone(response_data["employee"]["manager_id"])
        self.assertTrue(response_data["employee"]["is_active"])

    def test_list_employee(self):
        employee_data1 = {
            "first_name": "aryan",
            "last_name": "satija",
            "email": "aryan.satija@gmail.com",
            "password": "smile",
            "role": "software engineer",
            "manager": None,
            "is_active": True,
        }
        employee1 = EmployeeDataStore.create_employee(self.company.id, employee_data1)

        employee_data2 = {
            "first_name": "vasu",
            "last_name": "sharma",
            "email": "vasu.sharma@gmail.com",
            "password": "smile",
            "role": "software engineer",
            "manager": employee1.id,
            "is_active": True,
        }
        EmployeeDataStore.create_employee(self.company.id, employee_data2)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(create_access_token(employee1.id))}"
        )
        url = f"/api/core/companies/{self.company.id}/employees/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(len(response_data), 2)

    def test_delete_employee(self):
        data = {
            "first_name": "aryan",
            "last_name": "satija",
            "email": "aryan.satija@gmail.com",
            "password": "smile",
            "role": "software engineer",
            "manager": None,
            "is_active": True,
        }

        employee = EmployeeDataStore.create_employee(self.company.id, data)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(create_access_token(employee.id))}"
        )
        url = f"/api/core/companies/{self.company.id}/employees/{employee.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

        with self.assertRaises(Employee.DoesNotExist):
            EmployeeDataStore.get_employee(employee.id)

    def test_update_employee(self):
        data = {
            "first_name": "aryan",
            "last_name": "satija",
            "email": "aryan.satija@gmail.com",
            "password": "smile",
            "role": "software engineer",
            "manager": None,
            "is_active": True,
        }

        employee = EmployeeDataStore.create_employee(self.company.id, data)

        updated_data = {
            "first_name": "aryan",
            "last_name": "satija",
            "email": "aryan.satija@gmail.com",
            "role": "software engineer 2",
            "manager": None,
            "is_active": True,
        }
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {str(create_access_token(employee.id))}"
        )

        url = f"/api/core/companies/{self.company.id}/employees/{employee.id}/"
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["role"], updated_data["role"])
