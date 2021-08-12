from faker import Faker

from hr.contacts import AddressBook
from hr.hr import PayrollSystem
from hr.productivity import ProductivitySystem

fake = Faker(["en_US", "en_GB", "en_IE"])


class EmployeeDatabase:
    def __init__(self) -> None:
        self._employees = [
            {"id": 1, "name": fake.name(), "role": "manager"},
            {"id": 2, "name": fake.name(), "role": "secretary"},
            {"id": 3, "name": fake.name(), "role": "sales"},
            {"id": 4, "name": fake.name(), "role": "factory"},
            {"id": 5, "name": fake.name(), "role": "secretary"},
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


class Employee:
    def __init__(
        self, id: int, name: str, address: str, role: str, payroll: PayrollSystem
    ) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.work(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print("")
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
