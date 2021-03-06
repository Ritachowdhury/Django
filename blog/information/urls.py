from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^districts/', views.district_list, name='districts'),
    url(r'^divisions/', views.division_list, name='divisions'),
    url(r'^dists-of-div/(?P<div_id>[0-9]+)/', views.dists_of_division,name = 'dists_of_division'),

    # url(r'^post-list/', views.post_list,name='post-list'),
    # url(r'^single-post/(?P<post_id>[0-9]+)/', views.single_post,name='single-post'),
]
