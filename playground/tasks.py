from time import sleep
from celery import shared_task


@shared_task
def notify_customer(message):
    print('sending 10k mail...')
    print(message)
    sleep(5)
    print('10k mail sent!')