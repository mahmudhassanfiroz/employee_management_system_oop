
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
    
