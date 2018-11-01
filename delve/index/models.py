from django.db import models


class Commodity(models.Model):
    commodity = models.CharField(max_length=15, verbose_name='Commodity')

    def __str__(self):
        return self.commodity


class Method(models.Model):
    method = models.CharField(max_length=15, verbose_name='Method')

    def __str__(self):
        return self.method


# Create your models here.
class Person(models.Model):
    initials = models.CharField(max_length=5, verbose_name='initals')
    name = models.CharField(max_length=100, verbose_name='full name')
    department =  models.CharField(max_length=100, verbose_name='department')
    commodity = models.ManyToManyField(Commodity)
    method = models.ManyToManyField(Method)
    
    def __str__(self):
        return self.initials

