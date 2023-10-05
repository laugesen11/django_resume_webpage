from django.db import models
from django.urls import reverse

# Entry for an education certification
class Education(models.Model):
    # Optional picture 
    picture = models.ImageField(upload_to='education_images', null=True, blank=True)

    # Name of certification/degree
    achievement = models.CharField(max_length=150)

    # Name of Institution (optional)
    institution = models.CharField(max_length=200, null=True, blank=True)

    # The year this was achieved
    date_achieved = models.DateField()

    # Valid until (If applicable)
    valid_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{achievement}"

    def get_absolute_url(self):
        return reverse('list_education')

    class Meta:
        ordering = ['-date_achieved']
