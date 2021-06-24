from django.db import models

class Indication(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    list_category = (
        ('1', 'Movie')
        ('2', 'Video')
        ('3', 'Book')
        ('4', 'Podcast')
        ('5', 'Activity')
    )
    category = models.CharField(max_length=30, choices=list_category, verbose_name='Category') 
			
    def __str__(self):
    	return self.title
