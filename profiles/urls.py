from django.urls import path,include
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile_view, name='profile')
]

