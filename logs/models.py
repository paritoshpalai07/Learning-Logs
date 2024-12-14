from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic
    
class Entry(models.Model):
    entry = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
