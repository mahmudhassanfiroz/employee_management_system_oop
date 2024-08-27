
from payroll import Payroll
class ReportGenerator:
    def generate_monthly_salary_report(self, employees, basic_salary, bonus=0, deductions=0):
        print("Monthly Salary Report")
        for emp in employees:
            payroll = Payroll(emp, basic_salary, bonus, deductions)
            print(f"{emp.name} - Net Salary: {payroll.calculate_payroll()}")

