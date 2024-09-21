from utils.config import EMAIL_HOST, EMAIL_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD
import smtplib
from email.mime.text import MIMEText

class AlertSystem:
    def __init__(self):
        self.email_host = EMAIL_HOST
        self.email_port = EMAIL_PORT
        self.email_address = EMAIL_ADDRESS
        self.email_password = EMAIL_PASSWORD

    def send_shipment_delay_alert(self, item_id, delay_duration):
        recipient_email = "bhavyashreev123@gmail.com"
        subject = f"Alert: Shipment Delay for Item {item_id}"
        message = f"Shipment of Item {item_id} delayed by {delay_duration} hours."
        
        self.send_email(recipient_email, subject, message)

    def send_email(self, recipient_email, subject, message):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.email_address
        msg["To"] = recipient_email

        try:
            with smtplib.SMTP(self.email_host, self.email_port) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.sendmail(self.email_address, recipient_email, msg.as_string())
            
            print(f"Alert email sent to {recipient_email}.")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
