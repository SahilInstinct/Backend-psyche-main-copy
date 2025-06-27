from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    mbti_type = models.CharField(max_length=10, blank=True)
    # Mind
    mind_introversion = models.FloatField(default=0.0)
    mind_extraversion = models.FloatField(default=0.0)

    # Energy
    energy_intuition = models.FloatField(default=0.0)
    energy_sensing = models.FloatField(default=0.0)

    # Nature
    nature_thinking = models.FloatField(default=0.0)
    nature_feeling = models.FloatField(default=0.0)

    # Tactics
    tactics_judging = models.FloatField(default=0.0)
    tactics_prospecting = models.FloatField(default=0.0)

    # Identity
    identity_assertive = models.FloatField(default=0.0)
    identity_turbulent = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username







admin.site.register(Profile)
