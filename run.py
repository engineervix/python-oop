#!/usr/bin/env python3
import json

from hr.employees import EmployeeDatabase
# from hr.hr import HourlyPolicy, PayrollSystem
# from hr.productivity import ProductivitySystem

# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees()

# manager = employees[0]
# manager.payroll = HourlyPolicy(55)

# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)


def print_dict(d):
    print(json.dumps(d, indent=2))


for employee in employees:
    print_dict(employee.to_dict())
