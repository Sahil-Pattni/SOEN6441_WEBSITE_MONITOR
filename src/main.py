# %%
from email_client import EmailClient
from monitor import WebpageMonitor
import time
import redis
import os

env = os.environ

def redis_connect() -> redis.Redis:
    """
    Connect to redis instance.

    Returns:
        redis.Redis: Redis instance.
    """
    try:
        r = redis.Redis(
            host=env['REDIS_HOST'],
            port=29160,
            password=env['REDIS_PASSWORD'],
            ssl=True,
            ssl_cert_reqs=None)
        return r
    except Exception as e:
        print(f'REDIS Instance Error: {e}')


def get_emails(r) -> list:
    """
    Get emails from redis instance.

    Args:
        r (redis.Redis): Redis instance.

    Returns:
        list: List of emails.
    """
    try:
        emails = r.lrange('emails', 0, -1)
        return [x.decode('utf-8') for x in emails]
    except Exception as e:
        print(f'Error retrieving emails: {e}')


def add_email(r, email) -> None:
    """
    Add email to redis instance.

    Args:
        r (redis.Redis): Redis instance.
        email (str): Email to add.
    """
    try:
        r.rpush('emails', email)
    except Exception as e:
        print(f'Error adding email: {e}')


def delete_user(r, user) -> None:
    """
    Delete user from redis instance.

    Args:
        r (redis.Redis): Redis instance.
        user (str): User to delete.
    """
    try:
        r.lrem('emails', 0, user)
    except Exception as e:
        print(f'Error deleting user: {e}')


# %%
if __name__ == '__main__':
    # Set recipients
    print(f'Script started at {time.ctime()}')
    # Get redis instance
    r = redis_connect()
    # Get emails
    recipients = get_emails(r)
    # Create monitor object
    monitor = WebpageMonitor(recipients, verbose=True)
    # Run monitor
    monitor.monitor_webpage()
    print('LOG: Monitored successfully.')