import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

env = os.environ

class EmailClient:
    def __init__(self, recipients: list):
        self.recipients = recipients
        self.port = 465
    
    def send_email(self, message):
        # Create a secure SSL context
        context = ssl.create_default_context()

        for recipient in self.recipients:
            with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
                server.login(env['SENDER_EMAIL'], env['EMAILPASSWORD'])
                server.sendmail(env['EMAILADDRESS'], recipient, message)