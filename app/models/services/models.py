from django.db import models

class User(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	eventsIn = models.ManyToManyField('Event')
	experienceIn = models.ManyToManyField('Experience')
	friends = models.ManyToManyField("self")
	def __str__(self):              # __unicode__ on Python 2
        	return self.firstName + " " + self.lastName

class Event(models.Model):

	datetime = models.DateTimeField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	experience = models.ForeignKey('Experience', on_delete=models.CASCADE, null = True)
	createdBy = models.ForeignKey('User', on_delete=models.CASCADE, null = True)
	def __str__(self):              # __unicode__ on Python 2
       		return self.title

class Experience(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
	createdBy = models.ForeignKey('User', on_delete=models.CASCADE, null = True)
	def __str__(self):              # __unicode__ on Python 2
        	return self.title

class Authenticator(models.Model):
	user_id = models.CharField(max_length=50)
	authenticator = models.CharField(max_length=255, primary_key=True, unique=True)
	date_created = models.DateTimeField(auto_now_add=True, blank=True)
