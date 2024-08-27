
import smtplib
from email.mime.text import MIMEText

class NotificationSystem:
    def send_email(self, to_email, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'admin@gmail.com'
        msg['To'] = to_email
    
        # Setup the server
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login('username', 'password')
        
        # Send the email
        server.sendmail('admin@gmail.com', to_email, msg.as_string())
        server.quit()
        
        print(f"Notification sent to {to_email}")
        