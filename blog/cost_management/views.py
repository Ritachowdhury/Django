# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Expense,StudentInfo
from .forms import ExpenseForm,StudentForm

from django.shortcuts import render,redirect

# Create your views here.
def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses':expenses}
    return render(request,'cost/expense.html',context)

def add_expense(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('cost-list')

    else:
        form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form': form})

def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form  = ExpenseForm(request.POST, instance=expense)
        form.save()
        return redirect('cost-list')
    else:
        form = ExpenseForm(instance=expense)
    context = {'form':form}
    return render(request, 'cost/edit_expense.html', context)


def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('cost-list')

def student_list(request):
    all_stu = StudentInfo.objects.all()
    context = {'all_stu':all_stu }
    return render(request,'student_info/student_list.html',context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        return redirect('student-list')
    else:
        form = StudentForm
    return render(request,'student_info/add_student.html',{'form':form})

def edit_student(request, expense_id):
    expense = StudentInfo.objects.get(id=expense_id)
    if request.method == 'POST':
        form  = StudentForm(request.POST, instance=expense)
        form.save()
        return redirect('student-list')
    else:
        form = StudentForm(instance=expense)
    context = {'form':form}
    return render(request, 'student_info/edit_student.html', context)

def delete_student(request,expense_id):
    expense = StudentInfo.objects.get(id=expense_id)
    expense.delete()
    return redirect('student-list')