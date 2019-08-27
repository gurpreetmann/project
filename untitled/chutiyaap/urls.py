

from django.contrib import admin
from django.urls import path,include
from .views import Avinash
from django.conf.urls import url

urlpatterns = [
    url('',Avinash.as_view())
]

