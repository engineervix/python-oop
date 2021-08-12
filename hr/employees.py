from hr.hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
from hr.productivity import ManagerRole, SecretaryRole, SalesRole, FactoryRole


class Employee:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.address = None


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id: int, name: str, weekly_salary: int) -> None:
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id: int, name: str, weekly_salary: int) -> None:
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id: int, name: str, weekly_salary: int, commission: int) -> None:
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)


class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id: int, name: str, hours_worked: int, hour_rate: int) -> None:
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id: int, name: str, hours_worked: int, hour_rate: int) -> None:
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)
