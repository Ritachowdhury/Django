from django.conf.urls import url
from .views import item_list

urlpatterns = [
    url(r'^list/',item_list,name='item-list'),
]
