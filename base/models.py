from django.db import models
from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField


# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_date', '-created_date']

    def __str__(self):
        return self.name
    

class Topic(models.Model):
    topic_name = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)
    url = EmbedVideoField()
    summary = models.TextField(blank=True, null=True)
    transcript = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    
    def __str__(self):
        return self.topic_name
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

class Doubt(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    doubt = models.TextField()
    creator = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doubt[:50]

class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.quote} - {self.author}'
    

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='hosted_rooms')
    topic = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True, related_name='topic_rooms')
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at',]


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.body[0:50]

class ToDoList(models.Model):
    listItem = models.TextField()
    listOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('completed','Completed'),
        ('incomplete','Incomplete'),
        ('ongoing','Ongoing'),
    ]

    listItemStatus = models.CharField(max_length=10, choices=STATUS_CHOICES, default='incomplete')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.listItem
    
    class Meta:
        ordering = ['-updated_at', '-created_at']