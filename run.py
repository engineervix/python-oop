#!/usr/bin/env python3
from hr.employees import employee_database
from hr.hr import LTDPolicy, calculate_payroll
from hr.productivity import track

employees = employee_database.employees()

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)
