from django.db import models

# The resource model is simplified currently for development
class Resource(models.Model):
	type = models.CharField(max_length=20)
	energy = models.IntegerField()
	
	# This enables me to call the model and get its type
	def __str__(self):
		return self.type