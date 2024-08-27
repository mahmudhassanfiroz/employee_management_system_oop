
class Attendance:
    def __init__(self, employee, date, status):
        self.employee = employee
        self.date = date
        self.status = status
    
    def mark_attendance(self):
        print(f"{self.employee.name}'s attendance on {self.date}: {self.status}")

class Leave:
    def __init__(self, employee, start_date, end_date, reason):
        self.employee = employee 
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
    
    def apply_leave(self):
        print(f"{self.employee.name} has applied for leave from {self.start_date} to {self.end_date} for {self.reason}.")

