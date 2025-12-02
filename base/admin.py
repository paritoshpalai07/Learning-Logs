from django.contrib import admin
from .models import Note, Quotes, Topic, Room, Message, ToDoList

# Register your models here.
admin.site.register(Note)
admin.site.register(Quotes)
admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(ToDoList)