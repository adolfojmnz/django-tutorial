from django.db import models


# Models for the membership example
class Musician(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name


class Band(models.Model):
	name = models.CharField(max_length=128)
	genre = models.CharField(help_text="Band's primary genre", max_length=60)
	members = models.ManyToManyField(Musician, through='Membership')


class Membership(models.Model):
	musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	join_year = models.IntegerField(null=True)
	invite_reason = models.CharField(max_length=64)
