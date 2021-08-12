#!/usr/bin/env python3
import json

from hr.employees import employee_database, Employee
from hr.hr import calculate_payroll
from hr.productivity import track


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees()

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print("Temporary Secretary:")
print_dict(temp_secretary.to_dict())
