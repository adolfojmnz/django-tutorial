from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Question, Choice


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'question_list' # default's

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]


class DetailsView(generic.DetailView):
	model = Question
	template_name = 'polls/poll_detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/poll_results.html'


def poll_vote(request, question_id):
	template_name = 'polls/poll_detail.html'
	question = get_object_or_404(Question, pk=question_id)

	try:
		selected_choice = question.choice_set.get(
			pk=request.POST['choice']
		)
		selected_choice.votes += 1
		selected_choice.save()
	except (KeyError, Choice.DoesNotExist):
		context = {
			'question': question,
			'error_message': 'Select an option!'
		}
		return render(request, template_name, context)

	return HttpResponseRedirect(
		reverse(
			'polls:results', args=(question.id,)
		)
	)
