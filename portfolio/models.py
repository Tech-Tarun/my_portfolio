from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=50,default='',null=False)
    email=models.CharField(max_length=80,default='',null=False)
    subject=models.CharField(max_length=50,default='',null=False)
    message=models.CharField(max_length=500,default='',null=False)
