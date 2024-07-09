from django.db import models

# Create your models here.

class Department(models.Model):
    lead = models.ForeignKey('Employee', on_delete=models.PROTECT, related_name='+', null=True)
    name = models.CharField(max_length=90)
    active = models.BooleanField(default=True)


class Employee (models.Model) :
    name = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    address = models.CharField(max_length=200) 
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
