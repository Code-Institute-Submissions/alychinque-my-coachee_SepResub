from django.db import models

class Indication(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    list_category = (
        ('Movie', 'Movie'),
        ('Video', 'Video'),
        ('Book', 'Book'),
        ('Podcast', 'Podcast'),
        ('Activity', 'Activity'),
    )
    category = models.CharField(max_length=30, choices=list_category, verbose_name='Category') 
			
    def __str__(self):
    	return self.title

