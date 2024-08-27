
class Employee:
    def __init__(self, name, employee_id, designation, department, salary):
        self.name = name 
        self.employee_id = employee_id
        self.designation = designation
        self.department = department
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Designation: {self.designation}, selary: {self.salary}")
    
    def update_info(self, name=None, designation=None, department=None, salary=None):
        if name:
            self.name = name
        if designation:
            self.designation = designation
        if department:
            self.department = department
        if salary:
            self.salary = salary
    
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, designation, department, salary, benefits):
        super().__init__(name, employee_id, designation, department, salary)
        self.benefits = benefits
    
    def display_info(self):
        super().display_info()
        print(f"Benefits: {self.benefits}")
    
class PartTimeEmployee(Employee):
        def __init__(self, name, employee_id, designation, department, hourly_rate):
            super().__init__(name, employee_id, designation, department, hourly_rate*20)
            self.hourly_rate = hourly_rate
        
        def display_info(self):
            super().display_info()
            print(f"Hourly Rate: {self.hourly_rate}")

class ContractEmployee(Employee):
    def __init__(self, name, employee_id, designation, department, contract_amount):
        super().__init__(name, employee_id, designation, department, contract_amount)
        self.contract_amount = contract_amount
    
    def display_info(self):
        super().display_info()
        print(f"Contract Amount: {self.contract_amount}")
