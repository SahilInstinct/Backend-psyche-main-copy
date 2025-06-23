from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    aspect = models.CharField(max_length=50)
    trait_if_agree = models.CharField(max_length=20)
    weight = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return self.question_text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti_type = models.CharField(max_length=10, blank=True, null=True)
    percentages = models.TextField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()






























































