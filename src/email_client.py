import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

env = os.environ

class EmailClient:
    def __init__(self, recipients: list, verbose=False) -> None:
        self.recipients = recipients
        self.port = 465
        self.sender_email = env['SENDER_EMAIL']
        self.sender_password = env['EMAILPASSWORD']
        self.verbose = verbose
    
    def __log(self, message):
        if self.verbose:
            print(f'LOG: {message}')

    def send_email(self, message):
        """
        Sends an email to the recipients with the specified message.
        Args:
            message (str): The message to send.
        """
        # Create a secure SSL context
        context = ssl.create_default_context()
        self.__log('Sending emails...')

        for recipient in self.recipients:
            with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient, message)
                self.__log(f'Sent email from {self.sender_email} to {recipient}')