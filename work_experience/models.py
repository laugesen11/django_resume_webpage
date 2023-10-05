from django.db import models
from django.urls import reverse

# Create your models here.
class WorkExperience(models.Model):
    # Optional image for work experience
    picture = models.ImageField(upload_to='work_images', null=True, blank=True)

    # The company name
    company = models.CharField(max_length=140)

    # The team name
    team_name = models.CharField(max_length=300) 
 
    # Your title at the job
    job_title = models.CharField(max_length=140)

    # The date you started this job
    start_date = models.DateField()

    # The date this job ended (optional)
    end_date = models.DateField(null=True, blank=True)

    # What you actually did at this job. TextField to be as long as you'd like
    work = models.TextField()

    def __str__(self):
        return f"{self.job_title} - {self.company}"

    # Uncomment out when ready
    def get_absolute_url(self):
        return reverse('list_work_experiences')

    class Meta:
        ordering = ['-start_date', '-end_date']
