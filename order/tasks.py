import random

from celery import shared_task
from django.contrib.auth import get_user_model

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
    random_employee = random.choice(employees)
    Order.objects.create(
        name=f"Task-{new_task_id}",
        description=f"Description for task-{new_task_id}",
        employee=random_employee
    )
