from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.FlashLoginView.as_view(), name='login'),
    path('profile/<pk>', login_required(views.ProfileView.as_view()), name='profile'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('edit_post/<pk>', views.EditPostView.as_view(), name='edit_post'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('delete_post/', views.DeletePostView.as_view(), name='delete_post'),
    path('like/', views.LikeView.as_view(), name='like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
