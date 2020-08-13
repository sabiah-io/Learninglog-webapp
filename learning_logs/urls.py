from django.urls import path

from learning_logs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete/<int:topic_id>/', views.delete, name='delete'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]