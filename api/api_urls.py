from django.urls import path
from . import api_views

urlpatterns = [
  path("get/", api_views.getData),
  path("post/", api_views.addData),
              ]

