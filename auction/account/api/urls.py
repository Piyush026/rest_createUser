from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from account.api import views

app_name = 'account_api'
urlpatterns =[
    path('register', views.registration_view, name='index'),
]