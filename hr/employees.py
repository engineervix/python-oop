from faker import Faker

from hr.contacts import get_employee_address
from hr.hr import get_policy
from hr.productivity import get_role
from hr.representations import AsDictionaryMixin

fake = Faker(["en_US", "en_GB", "en_IE"])


class _EmployeeDatabase:
    def __init__(self) -> None:
        self._employees = {
            1: {"name": fake.name(), "role": "manager"},
            2: {"name": fake.name(), "role": "secretary"},
            3: {"name": fake.name(), "role": "sales"},
            4: {"name": fake.name(), "role": "factory"},
            5: {"name": fake.name(), "role": "secretary"},
        }

    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError("invalid employee_id")
        return info


class Employee(AsDictionaryMixin):
    def __init__(self, id: int) -> None:
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get("name")
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get("role"))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.work(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print("")
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


employee_database = _EmployeeDatabase()
