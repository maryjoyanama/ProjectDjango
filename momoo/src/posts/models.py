from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
	database_name = models.CharField(max_length=200)
	process_name = models.CharField(max_length=200)
	lastcomplete_date = models.DateTimeField(default=datetime.now, blank=True)
	status = models.CharField(max_length=10)
	issuspended = models.CharField(max_length=10)
	interval = models.IntegerField()
	average = models.IntegerField()
	laginseconds = models.IntegerField()
	def __str__(self):
		return self.database_name
	class Meta:
		verbose_name_plural = "Posts"
	