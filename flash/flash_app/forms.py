from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import FlashUser, Post


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'w-full form-input p-1 border-neutral-700 border focus:border-neutral-700 focus:outline focus:outline-1 shadow w-1/4 rounded'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'w-full form-input p-1 border-neutral-700 border focus:border-neutral-700 focus:outline focus:outline-1 shadow w-1/4 rounded'})
    class Meta:
        model = FlashUser
        fields = ['username', 'full_name', 'email', 'avatar', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full form-input border-neutral-700 p-1 border focus:border-neutral-700 focus:outline focus:outline-1 shadow- w-1/4 rounded'}),
            'full_name': forms.TextInput(attrs={'class': 'w-full form-input border-neutral-700 p-1 border focus:border-neutral-700 focus:outline focus:outline-1 shadow w-1/4 rounded'}),
            'email': forms.EmailInput(attrs={'class': 'w-full form-input border-neutral-700 p-1 border focus:border-neutral-700 focus:outline focus:outline-1 shadow w-1/4 rounded'}),
            'avatar': forms.FileInput(attrs={'class': 'w-full form-input border-neutral-400 shadow focus:border-neutral-700 focus:outline focus:outline-1 w-1/4 cursor-pointer border rounded'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full form-input p-1 shadow focus:border-neutral-700 focus:outline focus:outline-1 border-neutral-700 border w-1/4 rounded'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'w-full form-input p-1 border-neutral-700 focus:border-neutral-700 focus:outline focus:outline-1 shadow border w-1/4 rounded'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'images']
