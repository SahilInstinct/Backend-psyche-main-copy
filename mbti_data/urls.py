from django.urls import path
from . import views

urlpatterns = [
    # Explore all MBTI types
    path("", views.explore_grid, name="explore_grid"),
    # MBTI Sections
    path("<str:code>/introduction/", views.show_introduction, name="mbti_intro"),
    path('<str:code>/relationship/', views.show_relationship, name='mbti_relationship'),
    path('<str:code>/friendship/', views.show_friendship, name='mbti_friendship'),
    path('<str:code>/parenthood/', views.show_parenthood, name='mbti_parenthood'),
    path('<str:code>/career/', views.show_career_path, name='mbti_career_path'),
    path('<str:code>/workplace/', views.show_workplace_habits, name='mbti_workplace_habits'),
    path('<str:code>/conclusion/', views.show_conclusion, name='mbti_conclusion'),
    # path("explore/<str:code>/career/", views.show_career, name="mbti_career"),
]