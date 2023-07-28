from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.files import File
from pathlib import Path

from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegistrationForm, LoginForm, PostForm

from .models import Post, Comment, FlashUser, Follower, Like

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-create_date')
        context['add_post_form'] = PostForm()
        return context

    def post(self, request, **kwargs):
        data = request.POST
        if 'file' in request.FILES:
            file = request.FILES['file']
            path = Path("./media/images/posts/upload.png")
            
            with path.open('wb') as img:
                img.write(file.read())
        if 'title' in data.keys():
            path = Path("./media/images/posts/upload.png")
            with path.open('rb') as image:
                img = File(image, name=image.name)
                post = Post(title=data['title'], text=data['text'], author=request.user, images=img)
                post.save()
                return JsonResponse({'post': render_to_string('macros/post.html', {'post': post, 'main': True, 'request': request})}, safe=False)
        return JsonResponse({'status': 500}, safe=False)

class EditPostView(UpdateView):
    template_name = 'index.html'
    model = Post
    fields = ['title', 'text']
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        if 'new_title' in data.keys():
            post = Post.objects.get(id=data['id'])
            post.title = data['new_title']
            post.text = data['new_text']
            post.save()
            return JsonResponse({'title': data['new_title'], 'text': data['new_text']}, safe=False)
        return JsonResponse({'status': 500})

class DeletePostView(DeleteView):
    model = Post

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        if 'post' in data.keys():
            
            Post.objects.get(id=data['post']).delete()
            return JsonResponse({'id': data['post']})
        return JsonResponse({'status': 500}, safe=False)

class LikeView(CreateView):
    model = Like
    fields = ['post']

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        if 'like' in data.keys():
            post = Post.objects.get(id=data['post'])
            like = Like(author=request.user, post=post)
            like.save()
            post.likes.add(like)
            return JsonResponse({'id': post.id}, safe=False)
        if 'unlike' in data.keys():
            post = Post.objects.get(id=data['post'])
            like = Like.objects.get(author=request.user, post=post)
            like.delete()
            return JsonResponse({'id': post.id}, safe=False)
        return JsonResponse({'status': 500}, safe=False)

class CommentView(CreateView):
    model = Comment
    fields = ['text']

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        if 'comment' in data.keys():
            comment = Comment(text=data['comment'], author=request.user)
            comment.save()
            Post.objects.get(id=data['post']).comments.add(comment)
            return JsonResponse({'comment': render_to_string('macros/comment.html', {'comment': comment})}, safe=False)
        return JsonResponse({'satus': 500})

class RegistrationView(CreateView):
    template_name = 'auth/register.html'
    model = FlashUser
    form_class = RegistrationForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        usernames = [user.username for user in FlashUser.objects.all()]
        if(not form.cleaned_data['username'] in usernames):
            username = form.cleaned_data['username']
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            avatar = form.cleaned_data['avatar']
            user = FlashUser(username=username, full_name=full_name, email=email, avatar=avatar)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.add_message(self.request, 20, 'You have been successfully registered!')
            return redirect('/')
        else:
            messages.add_message(self.request, 40, 'User with that username already exists')
        return form



class ProfileView(DetailView):
    model = FlashUser
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user'] = kwargs['object']
        context['posts'] = Post.objects.filter(author=context['user'])
        context['followers'] = [follower.follower for follower in Follower.objects.filter(user=context['user']).all()]
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        if 'bio' in data.keys():
            request.user.bio = data['bio']
            request.user.save()
            return JsonResponse({'bio': data['bio']}, safe=False)
        if 'follow' in data.keys():
            user = FlashUser.objects.get(id=data['user'])
            follower = Follower(user=user, follower=request.user)
            follower.save()
            # user.follower.add(follower)
            # user.save()
        if 'unfollow' in data.keys():
            user = FlashUser.objects.get(id=data['user'])
            
            follower = Follower.objects.get(user=user, follower=request.user)
            follower.delete()
            user.save()
        return JsonResponse({'status': 500}, safe=False)

class FlashLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    form_class = LoginForm