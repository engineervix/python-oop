from typing import List


class _PayrollSystem:
    def __init__(self) -> None:
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9),
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError("invalid employee_id")
        return policy

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


class LTDPolicy:
    def __init__(self) -> None:
        self._base_policy = None

    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * 0.6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError("Base Policy Missing")


class PayrollPolicy:
    def __init__(self) -> None:
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary: int) -> None:
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate: int) -> None:
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary: int, commission_per_sale: int) -> None:
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        # we're assuming that they make a sale every 5 hours
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission()


_payroll_system = _PayrollSystem()


def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    return _payroll_system.calculate_payroll(employees)
