# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=150)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    data_ref = models.DateTimeField()

    def __str__(self):
        return self.name

# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     continent = models.CharField(max_length=100)
#     population = models.IntegerField()
#     qtd_medalhas = models.IntegerField()
#     sigla = models.CharField(max_length=5)
#
#     def __str__(self):
#         return self.name