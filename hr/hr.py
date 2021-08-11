from abc import ABC, abstractmethod
from typing import List


class PayrollSystem:
    def calculate_payroll(self, employees: List):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for {employee.id} - {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}")
            print("")


class Employee(ABC):
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id: int, name: str, weekly_salary: int) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id: int, name: str, hours_worked: int, hour_rate: int) -> None:
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id: int, name: str, weekly_salary: int, commission: int) -> None:
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
