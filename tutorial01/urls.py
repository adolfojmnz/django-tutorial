from django.urls import path

from .views import year_archive, month_archive, detail_archive


urlpatterns = [
        path('archive/<int:year>/', year_archive, name='year_archive'),
		path('archive/<int:year>/<int:month>/', month_archive, name='month_archive'),
		path('archive/<int:year>/<int:month>/<int:pk>/', detail_archive, name='detail_archive'),
]
