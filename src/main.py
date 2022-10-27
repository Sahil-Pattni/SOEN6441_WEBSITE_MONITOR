from email_client import EmailClient
from monitor import WebpageMonitor

if __name__ == '__main__':
    # Initialize email client
    recipients = ['sahilpattni97+SOENBOT@gmail.com']
    email_client = EmailClient(recipients)
    email_client.send_email('Hello world!')