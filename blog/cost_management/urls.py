from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^list/',views.my_expense, name='cost-list'),
    url(r'^add/',views.add_expense, name='add-expense'),
    url(r'^edit/(?P<expense_id>[0-9]+)/', views.edit_expense, name='edit-expense'),
    url(r'^delete/(?P<expense_id>[0-9]+)/', views.delete_expense, name='delete-expense'),
    url(r'^student/', views.student_list, name='student-list'),
    url(r'^add_stu/', views.add_student, name='add-student'),
    url(r'^editstu/(?P<expense_id>[0-9]+)/', views.edit_student, name='editstudent'),
    url(r'^delete-stu/(?P<expense_id>[0-9]+)/', views.delete_student, name='delete-student')
]