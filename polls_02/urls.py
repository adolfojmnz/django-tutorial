from django.urls import path

from .views import poll_vote, IndexView, DetailsView, ResultsView


app_name = 'polls'
urlpatterns = [
	path('polls/', IndexView.as_view(), name='index'),
	path('polls/<int:question_id>/vote/', poll_vote, name='vote'),
	path('polls/<int:pk>/details/', DetailsView.as_view(), name='details'),
	path('polls/<int:pk>/results/', ResultsView.as_view(), name='results'),
]
