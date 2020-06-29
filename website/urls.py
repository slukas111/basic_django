from django.urls import path
from website.views import *

urlpatterns = [
    path('', welcome, name= 'home'),
    path('date', date, name='date'),
    path('about', about, name='about'),
]

