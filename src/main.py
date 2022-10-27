from email_client import EmailClient
from monitor import WebpageMonitor
import time

if __name__ == '__main__':
    # Set recipients
    print(f'Script started at {time.ctime()}')
    recipients = ['sahilpattni97+SOENBOT@gmail.com']
    # Create monitor object
    monitor = WebpageMonitor(recipients, verbose=True)
    # Run monitor
    monitor.monitor_webpage()
    print('LOG: Monitored successfully.')