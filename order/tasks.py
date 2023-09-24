import random
import requests

from celery import shared_task

from django.contrib.auth import get_user_model
from kombu.exceptions import OperationalError

from Producer_Consumer_microservice.celery import app
from Producer_Consumer_microservice.settings import BOT_TOKEN
from order.models import Order

Employee = get_user_model()


@shared_task
def order_creation():
    last_task = Order.objects.order_by('-task_id').first()
    if last_task is None:
        new_task_id = 1
    else:
        new_task_id = last_task.task_id + 1
    employees = Employee.objects.all()
    if employees:
        random_employee = random.choice(employees)
        Order.objects.create(
            name=f"Task-{new_task_id}",
            description=f"Description for task-{new_task_id}",
            employee=random_employee
        )


@app.task()
def send_telegram_message(chat_id, message_text):
    try:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {'chat_id': chat_id, 'text': message_text}
        response = requests.post(url, data=data)
        print(response)
    except (ConnectionError, OperationalError):
        pass

