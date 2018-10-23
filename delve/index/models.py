from django.db import models

# Create your models here.
class Person(models.Model):
    initials = models.CharField(max_length=5, verbose_name='initals')
    name = models.CharField(max_length=100, verbose_name='full name')
    
