# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Expense(models.Model):
    amount = models.IntegerField()
    purpose = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.purpose

class StudentInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender_choices = (
    ('ma', 'Male'),
    ('fe', 'Female'),
    )
    gender = models.CharField(max_length=20,
        choices=gender_choices,
        default='ma')

    fathers_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.IntegerField()