from django.urls import path
from . import views

# URL patterns for the chat app
urlpatterns = [
    path('', views.index, name='index'),
    # '' = root of chat app, calls index view

    path('chat/', views.chat, name='chat'),
    # 'chat/' endpoint for POST requests

    path('api/news/feed', views.news_feed, name='news_feed'),
    # 'api/news/feed' endpoint for GET requests - fetches Wikipedia events
]