from django.urls import path
from .views import api

app_name = 'User'

urlpatterns = [
    path('', api, name='API')
]