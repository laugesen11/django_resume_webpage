from django.db import models
from django.urls import reverse

# Create your models here.
class Skillset(models.Model):

    # Picture emblem for skillset
    picture = models.ImageField(upload_to='skills_images', null=True, blank=True)  

    # Name of skillset
    skill = models.CharField(max_length=150)

    # Years of experience using/developing this skillset
    years = models.PositiveIntegerField()

    # Details of this skillset
    details = models.TextField()

    def __str__(self):
        return self.skill
 
    def get_absolute_url(self):
        return reverse('list_skillset')

    class Meta:
        ordering = ['-years']
