from django.db import models

class Experience(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
	def __str__(self):              # __unicode__ on Python 2
        	return self.title

class Event(models.Model):

	datetime = models.DateTimeField('date of event')
	price = models.DecimalField(max_digits=6, decimal_places=2)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	experience = models.ForeignKey(Experience, on_delete=models.CASCADE, null = True)
	def __str__(self):              # __unicode__ on Python 2
       		return self.title

class User(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	eventsIn = models.ManyToManyField(Event)
	experienceIn = models.ManyToManyField(Experience)
	def __str__(self):              # __unicode__ on Python 2
        	return self.firstName + " " + self.lastName