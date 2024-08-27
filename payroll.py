
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
        print(f"Net Salary: {self.calculate_payroll()}")

class FullTimePayroll(Payroll):
    def __init__(self, employee,basic_salary, bonus=0, deductions=0):
        super().__init__(employee,basic_salary,bonus,deductions)
    
    def calculate_payroll(self):
        return self.basic_salary + self.bonus - self.deductions

class PartTimePayroll(Payroll):
    def __init__(self, employee,hours_worked, bonus=0, deductions=0):
        super().__init__(employee, hours_worked, bonus, deductions)
        self.hours_worked = hours_worked
    
    def calculate_payroll(self):
        return self.hours_worked * self.hours_worked

class ContractPayroll(Payroll):
    def calculate_payroll(self):
        return self.employee.contract_amount 


        