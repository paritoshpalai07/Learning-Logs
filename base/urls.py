from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/listitem/<int:pk>/', views.deleteToDListItem, name='delete_todo'),
    path('delete/<int:pk>/', views.deleteNote, name='delete'),
    path('update/<int:pk>/', views.updateNote, name='update'),
    path('note/<int:pk>/', views.noteView, name='note_view'),
    path('note/<int:noteId>/topic/<int:topicId>/', views.noteTopicView, name='note_topic'),
    path('note/<int:noteId>/topic/<int:topicId>/delete/', views.topicDelete, name='topic-delete'),
    # path('rooms/', views.rooms, name='rooms'),
    path('room/<int:pk>/', views.roomView, name='room_view'),
    path('test/', views.test, name='test'),
]