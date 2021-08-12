from typing import List


class ProductivitySystem:
    def track(self, employees: List, hours: int):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
        print("")


class ManagerRole:
    def work(self, hours: int):
        return f"plans, organizes, directs and controls resources for {hours} hours."


class SecretaryRole:
    def work(self, hours: int):
        return f"maintains effective records and carries out administrative tasks for {hours} hours."


class SalesRole:
    def work(self, hours: int):
        return (
            f"sells retail products, goods and services to customers for {hours} hours."
        )


class FactoryRole:
    def work(self, hours: int):
        return f"operates machinery and tools for {hours} hours."
