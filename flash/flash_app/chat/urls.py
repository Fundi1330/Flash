from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('start_chat', login_required(views.StartChat.as_view()), name='start_chat'),
    path('chats', login_required(views.ChatsView.as_view()), name='chats'),
    path('chat/<chat_id>', login_required(views.ChatView.as_view()), name='chat')
]