
class Payroll:
    def __init__(self, employee, basic_salary, bonus=0, deductions=0):
        self.employee = employee
        self.basic_salary = basic_salary
        self.bonus = bonus
        self.deductions = deductions
    
    def calculate_payroll(self):
        return self.basic_salary + self.bonus - self.deductions

    def generate_payslip(self):
        print(f"Payslip for {self.employee.name} (ID: {self.employee.employee_id})")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Bonus: {self.bonus}")
        print(f"Deductions: {self.deductions}")
        print(f"Net Salary: {self.calculate_salary()}")

