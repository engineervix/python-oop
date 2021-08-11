from hr import hr, employees, productivity

manager = employees.Manager(1, "John Smith", 1500)
secretary = employees.Secretary(2, "Jane Doe", 1200)
sales_person = employees.SalesPerson(3, "Kevin Bacon", 1000, 250)
factory_worker = employees.FactoryWorker(4, "Pete Peterson", 40, 15)
temporary_secretary = employees.TemporarySecretary(5, "Robin Williams", 40, 9)

employees = [manager, secretary, sales_person, factory_worker, temporary_secretary]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
