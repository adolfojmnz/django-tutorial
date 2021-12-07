from django.db import models


class Person(models.Model):
	SHIRT_SIZES = (
	('S', 'Small'),
	('M', 'Medium'),
	('L', 'Large'),
	)

	name = models.CharField(max_length=60)
	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Runner(models.Model):
	MEDAL_TYPE = models.TextChoices('MEDAL_TYPE', 'GOLD SILVER BLONZE')

	name = models.CharField(max_length=60)
	medal = models.CharField(blank=True, choices=MEDAL_TYPE.choices, max_length=10)
