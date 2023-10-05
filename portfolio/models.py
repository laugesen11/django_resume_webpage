from django.db import models
from django.urls import reverse

# Display for code porfolio you are making
class Display(models.Model):
    # Optional image
    picture = models.ImageField(upload_to='portfolio_images', null=True, blank=True)

    # Details about the work you are linking to
    details = models.TextField()
  
    # Title of the work you are displaying
    title = models.CharField(max_length=200)
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list_display')


class CodeLinks(models.Model):
    # The URL we are linking to
    link_url = models.URLField(max_length=250)

    # The name we want to display for the URL
    info = models.CharField(max_length=200)
 
    # Attaches this link to a display
    display = models.ForeignKey(
        Display,
        on_delete=models.CASCADE,
        related_name='codelinks',
    )
 
    def __str__(self):
        return self.info   
 
    def get_absolute_url(self):
        return reverse('list_display')

