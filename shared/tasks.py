# myapp/tasks.py
from celery import shared_task


@shared_task
def send_welcome_email():
    print('send welcome email')
    return f'Email sent'
