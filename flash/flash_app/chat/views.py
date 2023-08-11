from typing import Any, Dict
from django.template.loader import render_to_string

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Chat, Message
from ..models import FlashUser, Post, Follower
from django.http import JsonResponse

# Create your views here.


class StartChat(ListView):
    model = FlashUser
    template_name = 'start_chat.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        following = [user.user for user in Follower.objects.all() if user.follower == self.request.user]

        for chat in Chat.objects.all():
            user = chat.members.filter().exclude(username=self.request.user.username).first()
            if user in following:
                following.pop(following.index(user))
        context['users'] = following
        return context
    
    def post(self, request, **kwargs):
        data = request.POST
        if 'id' in data.keys():
            user = FlashUser.objects.get(id=data['id'])
            if(not Chat.objects.filter(name=user.username, avatar=user.avatar, members__in=[request.user.id, user.id], author=request.user).exists()):
                new_chat = Chat(name=user.username, avatar=user.avatar, author=request.user)
                new_chat.save()
                new_chat.members.add(user)
                new_chat.members.add(request.user)
                chats = []
                for chat in Chat.objects.all():
                    if self.request.user in chat.members.all():
                        chats.append(chat)
                print(render_to_string('chat.html', {'users': FlashUser.objects.all(), 'chats': chats}))
                return JsonResponse({'chat': render_to_string('chat.html', {'users': FlashUser.objects.all(), 'chats': chats})}, safe=False)
            return JsonResponse({'status': 500}, safe=False)
        return JsonResponse({'status': 500}, safe=False)

class ChatsView(ListView):
    template_name = 'chats.html'
    model = Chat

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        chats = []
        for chat in Chat.objects.all():
            if self.request.user in chat.members.all():
                chat.name = chat.members.filter().exclude(username=self.request.user.username).first().username
                chat.avatar = chat.members.filter().exclude(username=self.request.user.username).first().avatar
                chat.save()
                chats.append(chat)
        context['chats'] = chats
        return context

class ChatView(TemplateView):
    template_name = 'chat.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        chats = []
        for chat in Chat.objects.all():
            if self.request.user in chat.members.all():
                chats.append(chat)

        context['chat'] = Chat.objects.get(id=kwargs['chat_id'])
        context['user'] = context['chat'].members.filter().exclude(username=self.request.user.username).first()
        context['chat_messages'] = Message.objects.filter(chat=context['chat']).all()
        return context

    def post(self, request, **kwargs):
        data = request.POST
        if 'msg' in data.keys():
            msg = Message(body=data['msg'], chat=Chat.objects.get(id=kwargs['chat_id']), author=request.user)
            msg.save()
            return JsonResponse({'message': render_to_string('macros/message.html', {'message': msg, 'user': request.user})}, safe=False)
    
        return JsonResponse({'status': 500}, safe=False)