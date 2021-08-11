from typing import List


class ProductivitySystem:
    def track(self, employees: List, hours: int):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
            print("")
