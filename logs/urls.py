from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<int:user_id>/', views.show_topics, name='show_topics'),
    path('topics/<int:user_id>/<int:topic_id>/', views.show_entries, name='show_entries'),
    path('new_topic/<int:user_id>/', views.new_topic, name='new_topic'),
    path('new_entry/<int:user_id>/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:user_id>/<int:topic_id>/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:user_id>/<int:topic_id>/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]