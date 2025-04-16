from django.db import models
import os
# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    departement = models.ForeignKey('Departement', on_delete=models.SET_NULL, null=True)  # ForeignKey ke Departement
    job_level = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    employment_status = models.CharField(max_length=50)
    join_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    day_payment = models.DecimalField(max_digits=10, decimal_places=0)

class Departement(models.Model):
    departement_name = models.CharField(max_length=100)

    def __str__(self):
        return self.departement_name

def certification_upload_path(instance, filename):
    return os.path.join('', filename)

class Certification(models.Model):
    certification_id = models.AutoField(primary_key=True)  # Auto-increment primary key
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    date_issued = models.DateField()
    verify_period = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=certification_upload_path, null=True, blank=True)