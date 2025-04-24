from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)


class TaskRestore(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)


class Contact(models.Model):
    name=models.CharField(max_length=50)
    phno=models.BigIntegerField()
    email=models.EmailField()
    suggestion=models.TextField()