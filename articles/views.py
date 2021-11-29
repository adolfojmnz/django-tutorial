from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    template_name = 'tutorial01/archive_list.html'
    context = {
        'year': year,
        'archive_list': Article.objects.filter(
			pub_date__year=year
		),
    }
    return render(request, template_name, context)


def month_archive(request, year, month):
	template_name = 'tutorial01/archive_list.html'
	context = {
		'year': year,
		'month': month,
		'archive_list': Article.objects.filter(
			pub_date__year=year,
			pub_date__month=month
		),
	}
	return render(request, template_name, context)


def detail_archive(request, year, month, pk):
	template_name = 'tutorial01/archive_detail.html'
	context = {
		'year': year,
		'month': month,
		'pk': pk,
		'archive_detail': Article.objects.get(pk=pk),
	}
	return render(request, template_name, context)
