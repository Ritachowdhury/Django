# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30)
    categoru = models.ForeignKey(Category,on_delete=None)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

