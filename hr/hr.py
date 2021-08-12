from typing import List


class PayrollSystem:
    def calculate_payroll(self, employees: List):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for {employee.id} - {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}")
            if employee.address:
                print("- Sent to:")
                print(employee.address)
            print("")


class SalaryPolicy:
    def __init__(self, weekly_salary: int) -> None:
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    def __init__(self, hours_worked: int, hour_rate: int) -> None:
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary: int, commission: int) -> None:
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
