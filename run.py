#!/usr/bin/env python3
from faker import Faker

from hr import hr, employees, productivity, contacts

fake = Faker(["en_US", "en_GB", "en_IE"])

manager = employees.Manager(1, fake.name(), 1500)
manager.address = contacts.Address(
    fake.street_address(),
    fake.city(),
    fake.state(),
    fake.postcode(),
    # fake.street_address()
)
secretary = employees.Secretary(2, fake.name(), 1200)
secretary.address = contacts.Address(
    fake.street_address(),
    fake.city(),
    fake.state(),
    fake.postcode(),
    # fake.street_address()
)
sales_person = employees.SalesPerson(3, fake.name(), 1000, 250)
factory_worker = employees.FactoryWorker(4, fake.name(), 40, 15)
temporary_secretary = employees.TemporarySecretary(5, fake.name(), 40, 9)

employees = [manager, secretary, sales_person, factory_worker, temporary_secretary]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
