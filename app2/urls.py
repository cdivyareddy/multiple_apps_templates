from django.urls import path
from app2.views import *
app_name='noyhing'

urlpatterns=[
    path('myself/',myself,name='myself')
]