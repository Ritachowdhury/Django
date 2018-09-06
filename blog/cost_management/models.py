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