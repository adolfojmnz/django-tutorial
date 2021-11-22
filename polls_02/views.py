from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def poll_index(request):
	template_name = 'polls/index.html'
	context = {
		'question_list': Question.objects.order_by('-pub_date')[:5]
	}
	return render(request, template_name, context)


def poll_details(request, question_id):
	template_name = 'polls/poll_detail.html'
	question = get_object_or_404(Question, pk=question_id)

	context = {
		'question': question,
	}
	return render(request, template_name, context)


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


def poll_results(request, question_id):
	template_name = 'polls/poll_results.html'
	context = {
		'question': get_object_or_404(
			Question, pk=question_id
		)
	}
	return render(request, template_name, context)
