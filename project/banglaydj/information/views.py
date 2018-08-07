# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Districts, Divisions

def district_list(request):
    div = Divisions.objects.get(name="Khulna")
    districts = Districts.objects.filter(division=div)
    context ={
        'districts':districts,
    }
    return render(request, 'info/districts.html', context)
def division_list(request):
    divisions = Divisions.objects.all()
    context ={
        'divisions':divisions,
    }
    return render(request, 'info/divisions.html', context)

def dists_of_division(request, div_id):
    division = Divisions.objects.get(pk=div_id)
    districts = Districts.objects.filter(division=division)
    context = {
        'districts': districts,
        'division': division,
    }
    return render(request, 'info/dists_of_division.html', context)