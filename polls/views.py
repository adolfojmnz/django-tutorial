from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'question_list' # default's

	def clean_queryset(self):
		""" Deletes questions without choices. """
		queryset = Question.objects.filter(
			pub_date__lte = timezone.now()
		)
		for q in queryset:
			if not q.choice_set.all():
				q.delete()
		return queryset

	def get_queryset(self):
		""" Returns the last 5 published polls. """
		return self.clean_queryset().order_by('-pub_date')[:5]


class DetailsView(generic.DetailView):
	model = Question
	template_name = 'polls/poll_detail.html'

	def get_queryset(self):
		""" Excludes questions yet to be published. """
		queryset = Question.objects.filter(
			pub_date__lte = timezone.now()
		)
		return queryset


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/poll_results.html'

	def get_queryset(self):
		""" Excludes questions yet to be published. """
		queryset = Question.objects.filter(
			pub_date__lte = timezone.now()
		)
		return queryset


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
