from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Order(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return self.name

