from django.utils import timezone
from django.db import models

from django.contrib import admin
from datetime import timedelta


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date 	  = models.DateField(default=timezone.now)

	@admin.display(
		boolean = True,
		ordering = 'pub_date',
		description = 'Published Recently'
	)

	def was_published_recently(self):
		now = timezone.now()
		day_before = now - timedelta(days=1)
		return now > self.pub_date > day_before

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question 	= models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes	    = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
