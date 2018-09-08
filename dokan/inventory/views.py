# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Item

from django.shortcuts import render

# Create your views here.
def item_list(request):
    all_items = Item.objects.all()
    context = {'all_items':all_items}
    return render(request,'inventory/item_list.html',context)