class Employee:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


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


class Manager(SalaryEmployee):
    def work(self, hours: int):
        print(
            f"{self.name} plans, organizes, directs and controls resources for {hours} hours."
        )


class Secretary(SalaryEmployee):
    def work(self, hours: int):
        print(
            f"{self.name} maintains effective records and carries out administrative tasks for {hours} hours."
        )


class SalesPerson(CommissionEmployee):
    def work(self, hours: int):
        print(
            f"{self.name} sells retail products, goods and services to customers for {hours} hours."
        )


class FactoryWorker(HourlyEmployee):
    def work(self, hours: int):
        print(f"{self.name} operates machinery and tools for {hours} hours.")


class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id: int, name: str, hours_worked: int, hour_rate: int) -> None:
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)
