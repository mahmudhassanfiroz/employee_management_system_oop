
from department import Department
from payroll import Payroll
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        self.departments = {}
    
    def add_employee(self, employee):
        self.employees.append(employee)
        if employee.department not in self.departments:
            self.departments[employee.department] = Department(employee.department)
        self.departments[employee.department].add_employee(employee)
    
    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]
        for dept in self.departments.values():
            dept.remove_employee(employee_id)
    
    def update_employee(self, employee_id, name=None, designation=None, department=None, salary=None):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                emp.update_info(name, designation, department, salary)
                return emp
        return None

    def display_all_employees(self):
        for emp in self.employees:
            emp.display_info()
    
    def display_department_info(self, department_name):
        if department_name in self.departments:
            self.departments[department_name].display_department_info()
        else:
            print(f"No department named {department_name} found.")
    
    def calculate_payroll(self, employee_id, basic_salary, bonus=0, deductions=0):
        for emp in self.employess:
            if emp.employee_id == employee_id:
                payroll = Payroll(emp, basic_salary, bonus, deductions)
                payroll.generate_payslip()
                return payroll
        print(f"Employee with ID {employee_id} not found.")
        return None
    