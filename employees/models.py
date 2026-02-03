from django.db import models
from accounts.models import User
from departments.models import Department

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
