from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=255)

    @classmethod
    def create_employee(cls):
        max_user = cls.objects.order_by('-id').first()
        if max_user is None:
            new_username = 1
        else:
            new_username = max_user.id + 1

        new_employee = cls(
            username="user" + str(new_username),
            probation=False,
            position="cto"
        )
        new_employee.save()

        return new_employee

    def __str__(self):
        return self.username


class Order(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="order")

    def __str__(self):
        return self.name

