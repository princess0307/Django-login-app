from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reg(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=30,default="none")

    def __str__(self):
        return self.name
