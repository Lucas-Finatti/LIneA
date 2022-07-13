from django.urls import path
from .views import get_titles, invalid_token_response

app_name = 'User'

urlpatterns = [
    path('', get_titles, name='GET_ALL_USERS'),
    path('access_denied/', invalid_token_response, name='ACCESS_DENIED')
]