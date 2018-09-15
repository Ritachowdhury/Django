"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.user_signup, name='signup'),
    url(r'^login/',views.user_login, name='login'),
    # url(r'^',views.home, name='home'),
    url(r'^logout/',views.user_logout, name='logout'),
    url(r'^blog/',include('blog_post.urls'), name='blog-home'),
    url(r'^cost/',include('cost_management.urls'), name='cost'),
    url(r'^user/',include('user_info.urls'), name='user'),
    url(r'^info/',include('information.urls'), name='information'),
]
