from django.db import models


class Department(models.Model):
    name = models.CharField(
        max_length=20,
    )


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    age = models.IntegerField()
    egn = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        verbose_name='EGN',
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
