from django.shortcuts import render

from .models import Question


def poll_list(request):
	template_name = 'polls/index.html'
	context = {
		'poll_list': Question.objects.all()
	}
	return render(request, template_name, context)


def poll_details(request, question_id):
	template_name = 'polls/poll_detail.html'
	context = {
		'question_id': question_id
	}
	return render(request, template_name, context)


def poll_results(request, question_id):
	template_name = 'polls/poll_results.html'
	context = {
		'question_id': question_id
	}
	return render(request, template_name, context)


def poll_vote(request, question_id):
	template_name = 'polls/poll_vote.html'
	context = {
		'question_id': question_id
	}
	return render(request, template_name, context)
