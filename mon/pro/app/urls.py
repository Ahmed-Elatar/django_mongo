from django.urls import path
from .views import *



urlpatterns = [
    path('', View.as_view() , name='index'),
]
