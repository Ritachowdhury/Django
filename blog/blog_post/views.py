# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.
# def home(request):
#     context= {
#         'name': 'rita',
#         'district': 'Khulna'
#     }
#     return render(request,'index.html',context)
def home(request):
    all_post = Post.objects.all()
    return render(request, 'index.html', {'all_post_list': all_post})

def post_list(request):
    post_list = Post.objects.all()
    context={
        'post_list':post_list,
    }
    return render(request,'post_list.html',context)
def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    print(post)
    return render(request,'single_post.html',{'post':post})