from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"