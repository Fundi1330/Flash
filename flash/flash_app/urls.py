from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .forms import LoginForm

urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.FlashLoginView.as_view(), name='login'),
    path('profile/<pk>', views.ProfileView.as_view(), name='profile'),
    path('logout', views.LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
