from django import forms
from .models import Expense,StudentInfo


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'