from django.urls import path

from .views import get_name, contact

app_name = 'users'
urlpatterns = [
	path('users/', get_name, name='name'),
	path('users/contact/', contact, name='contact')
]
