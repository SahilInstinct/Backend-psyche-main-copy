from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    aspect = models.CharField(max_length=50)
    trait_if_agree = models.CharField(max_length=20)
    weight = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return self.question_text


from django.contrib.auth.models import User


































































