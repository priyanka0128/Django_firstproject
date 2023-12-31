"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',v.home),
    path('first',v.first_page),
    path('second',v.second_page),
    path('register',v.adduser),
    path('add_user',v.Add_User),
    path('register1',v.adduser1),
    path('add_user1',v.Add_User1),
    path('ulist',v.User_list),
]
