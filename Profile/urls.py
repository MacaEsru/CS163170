from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from Profile import views

urlpatterns = [
    re_path(r'profile_list/$', views.ProfileList.as_view()),
    re_path(r'city/$', views.CityList.as_view()),
    re_path(r'occupation/$', views.OccupationList.as_view()),
    re_path(r'gender/$', views.GenderList.as_view()),
    re_path(r'marital_status/$', views.MaritalStatusList.as_view()),
    re_path(r'state/$', views.StateList.as_view()),
]