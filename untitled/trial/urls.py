from .views import mult
from django.conf.urls import url

urlpatterns = [
    url('',mult.as_view())
]
