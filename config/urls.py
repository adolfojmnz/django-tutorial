from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

	path('', include('articles.urls')),
	path('', include('polls.urls')),
	path('', include('users.urls')),
	path('', include('pages.urls')),
]
