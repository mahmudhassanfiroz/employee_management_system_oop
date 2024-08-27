
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employee_list = []
    
    def add_employee(self, employee):
        self.employee_list.append(employee)
    
    def remove_employee(self, employee_id):
        self.employee_list = [emp for emp in self.employee_list if emp.employee_id != employee_id]
    
    def display_department_info(self):
        print(f"Department Name: {self.department_name}")
        for emp in self.employee_list:
            emp.display_info()
    

        