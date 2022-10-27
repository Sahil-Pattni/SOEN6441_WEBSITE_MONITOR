from email_client import EmailClient
from monitor import WebpageMonitor
# %%
if __name__ == '__main__':
    # Set recipients
    recipients = ['sahilpattni97+SOENBOT@gmail.com']
    # Create monitor object
    monitor = WebpageMonitor(recipients, verbose=True)
    # Run monitor
    monitor.monitor_webpage()

# %%