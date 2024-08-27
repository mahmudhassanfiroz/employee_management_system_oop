
from management_system import EmployeeManagementSystem
from employee import Employee

def main():
    system = EmployeeManagementSystem()
    
    # Test Data
    emp1 = Employee("Alice", "E001", "Developer", "IT", 70000)
    emp2 = Employee("Bob", "E002", "Manager", "HR", 80000)
    
    system.add_employee(emp1)
    system.add_employee(emp2)
    
    system.display_all_employees()
    
    # Save data to file 
    # system.save_to_file()

if __name__ == "__main__":
    main()