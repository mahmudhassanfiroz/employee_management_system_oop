""" 
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
     """
from management_system import EmployeeManagementSystem
from employee import FullTimeEmployee, PartTimeEmployee, ContractEmployee
from attendance import Attendance
# from leave import Leave
from payroll import Payroll, FullTimePayroll, PartTimePayroll, ContractPayroll
from report import ReportGenerator
from notification import NotificationSystem

def main():
    system = EmployeeManagementSystem()
    
    # Test Data
    emp1 = FullTimeEmployee("Alice", "E001", "Developer", "IT", 70000, benefits="Health Insurance")
    emp2 = PartTimeEmployee("Bob", "E002", "Consultant", "HR", hourly_rate=1500)
    emp3 = ContractEmployee("Charlie", "E003", "Designer", "Design", contract_amount=50000)
    
    system.add_employee(emp1)
    system.add_employee(emp2)
    system.add_employee(emp3)
    
    system.display_all_employees()
    
    # Update employee info
    system.update_employee("E001", name="Alicia", salary=75000)
    system.display_all_employees()
    
    # Mark attendance
    attendance1 = Attendance(emp1, "2024-08-25", "Present")
    attendance1.mark_attendance()
    
    # Apply leave
    # leave1 = Attendance(emp2, "2024-08-28", "2024-08-30", "Medical Leave")
    # leave1.apply_leave()
    
    # Calculate and display payroll
    payroll1 = FullTimePayroll(emp1, basic_salary=75000, bonus=5000, deductions=2000)
    payroll1.generate_payslip()
    
    payroll2 = PartTimePayroll(emp2, hours_worked=80)
    payroll2.generate_payslip()
    
    payroll3 = ContractPayroll(emp3, 2000, 500)
    payroll3.generate_payslip()
    
    # Generate Monthly Salary Report
    report_generator = ReportGenerator()
    report_generator.generate_monthly_salary_report(system.employees, 2000, 500)
    
    # Send Notification
    # notifier = NotificationSystem()
    # notifier.send_email("alice@example.com", "Monthly Payslip", "Your payslip has been generated.")
    
    # Display department information
    system.display_department_info("IT")
    system.display_department_info("HR")
    system.display_department_info("Design")

if __name__ == "__main__":
    main()
