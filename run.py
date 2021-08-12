#!/usr/bin/env python3
from hr.employees import EmployeeDatabase
from hr.hr import PayrollSystem
from hr.productivity import ProductivitySystem

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees()

productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
