from django.urls import path

from .views import poll_index, poll_details, poll_vote, poll_results


app_name = 'polls'
urlpatterns = [
	path('polls/', poll_index, name='index'),
	path('polls/<int:question_id>/vote/', poll_vote, name='vote'),
	path('polls/<int:question_id>/details/', poll_details, name='details'),
	path('polls/<int:question_id>/results/', poll_results, name='results'),
]
