from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
  name = models.CharField(max_length=255,null=True)
  email = models.EmailField(null=True)
  password = models.CharField(max_length=20,null=True)
  phone_number = models.CharField(max_length=15, null=True)
  dob = models.DateField(null=True)
  def __str__(self):
    return f"{self.name}"


class Department(models.Model):
  name = models.CharField(max_length=100,null=True)
  description = models.TextField()
  
  def __str__(self):
    return self.name

class Role(models.Model):
  name = models.CharField(max_length=100,null=True)
  description = models.TextField()
  
  def __str__(self):
    return self.name


class Member(models.Model):
  # user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  employee_id = models.CharField(max_length=20,null=True)
  name = models.CharField(max_length=255,null=True)
  email = models.EmailField(null=True)
  password = models.CharField(max_length=20,null=True)
  phone_number = models.CharField(max_length=15, null=True)
  dob = models.DateField(null=True)
  # role = models.CharField(max_length=255, null=True)
  role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
  joining_date = models.DateField(null=True)
  team = models.CharField(max_length=255, null=True)
  reporting_manager = models.CharField(max_length=255, null=True)
  assigned_assets = models.TextField(null=True)
  allocated_tools = models.TextField(null=True)
  timeline = models.CharField(max_length=255, null=True)
  address = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255, null=True)
  # department = models.CharField(max_length=255, null=True)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return f"{self.name}"
