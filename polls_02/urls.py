from django.urls import path

from .views import poll_list, poll_details, poll_vote, poll_results


urlpatterns = [
	path('polls/', poll_list, name='poll_list'),
	path('polls/<int:question_id>/vote/', poll_vote, name='poll_vote'),
	path('polls/<int:question_id>/details/', poll_details, name='poll_details'),
	path('polls/<int:question_id>/results/', poll_results, name='poll_results'),
]
