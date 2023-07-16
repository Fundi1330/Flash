from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm, LoginForm

from .models import Post, Comment, FlashUser

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    
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
            password = form.cleaned_data['password1']
            user = FlashUser(username=username, full_name=full_name, password=password, email=email, avatar=avatar)
            user.save()
            return redirect('/')
        else:
            messages.add_message(self.request, 40, 'User with that username already exists')
        return form
    
class FlashLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    form_class = LoginForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        employee = FlashUser.objects.get(username=user)
        if employee.active:
            login(self.request, user) # since there's a variable up there
        return super().form_valid(form) # we can just return the normal form_valid which is also an HttpResponseRedirect


    