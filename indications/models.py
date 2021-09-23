from django.db import models

class Indication(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    list_category = (
        ('Movie', 'Movie'),
        ('Video', 'Video'),
        ('Book', 'Book'),
        ('Podcast', 'Podcast'),
        ('Activity', 'Activity'),
    )
    category = models.CharField(max_length=30, choices=list_category, 
                                verbose_name='Category', null=False, blank=False) 

    list_plans = {
        ('Premium', 'Premium'),
        ('Standard', 'Standard'),
        ('Basic', 'Basic'),
        ('Free', 'Free')
    }
    plan = models.CharField(max_length=10, null=False, blank=False, choices=list_plans, default='Free')

    def __str__(self):
    	return self.title

