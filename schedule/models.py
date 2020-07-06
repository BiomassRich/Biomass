from django.db import models
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def startTime(self):
        return self.start_time.strftime('%H:%M')
    @property
    def get_html_url(self):
        url = reverse('schedule:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} {self.startTime()} </a>'
    def __str__(self):
        return str(self.title) + " " + str(self.start_time) + " "  + str(self.end_time)
