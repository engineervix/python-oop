from typing import List


class ProductivitySystem:
    def __init__(self) -> None:
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError("invalid role_id")
        return role_type()

    def track(self, employees: List, hours: int):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
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
