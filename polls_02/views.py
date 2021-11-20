from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Question, Choice


def poll_list(request):
	template_name = 'polls/index.html'
	context = {
		'poll_list': Question.objects.order_by('-pub_date')[:5]
	}
	return render(request, template_name, context)


def poll_details(request, question_id):
	template_name = 'polls/poll_detail.html'
	question = get_object_or_404(Question, pk=question_id)
	choices = get_list_or_404(question.choice_set.all())

	context = {
		'question': question,
		'choices': choices,
	}
	return render(request, template_name, context)


def poll_results(request, question_id):
	template_name = 'polls/poll_results.html'
	context = {
		'question': get_object_or_404(
			Question, pk=question_id
		)
	}
	return render(request, template_name, context)


def poll_vote(request, question_id):
	template_name = 'polls/poll_vote.html'
	context = {
		'question': get_object_or_404(
			Question, pk=question_id
		)
	}
	return render(request, template_name, context)
