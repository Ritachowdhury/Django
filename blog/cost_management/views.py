# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Expense

from django.shortcuts import render

# Create your views here.
def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses':expenses}
    return render(request,'cost/expense.html',context)