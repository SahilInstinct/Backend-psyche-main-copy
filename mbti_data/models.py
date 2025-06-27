from django.db import models

# Create your models here.

ASPECT_CHOICES = [
    ('Introverted', 'Introverted'),
    ('Extraverted', 'Extraverted'),
    ('Intuitive', 'Intuitive'),
    ('Sensing', 'Sensing'),
    ('Thinking', 'Thinking'),
    ('Feeling', 'Feeling'),
    ('Judging', 'Judging'),
    ('Prospecting', 'Prospecting'),
]

class PersonalityType(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=20, default="#ffffff")
    hero_image = models.URLField(blank=True, null=True)
    aspect1 = models.CharField(max_length=20, choices=ASPECT_CHOICES,blank=True, null=True)
    aspect2 = models.CharField(max_length=20, choices=ASPECT_CHOICES,blank=True, null=True)
    aspect3 = models.CharField(max_length=20, choices=ASPECT_CHOICES, blank=True, null=True)
    aspect4 = models.CharField(max_length=20, choices=ASPECT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.code



#Introduction content table
class IntroductionPage(models.Model):
    personality = models.OneToOneField(PersonalityType, on_delete=models.CASCADE, related_name="introduction_page")

    description = models.TextField()
    mbti_quote = models.TextField(blank=True, null=True)

    text1 = models.TextField(blank=True, null=True)
    pic1 = models.URLField(blank=True, null=True)
    quote1 = models.TextField(blank=True, null=True)

    text2 = models.TextField(blank=True, null=True)
    subheading1 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)
    quote2 = models.TextField(blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)

    subheading2 = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)
    quote3 = models.TextField(blank=True, null=True)
    text6 = models.TextField(blank=True, null=True)

    subheading3 = models.CharField(max_length=255, blank=True, null=True)
    text7 = models.TextField(blank=True, null=True)
    quote4 = models.TextField(blank=True, null=True)
    text8 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.personality.code} - Introduction Page"

#Strength and weakness Table
class StrengthWeaknessPage(models.Model):
    personality = models.OneToOneField(PersonalityType, on_delete=models.CASCADE, related_name="strength_weakness_page")

    # Strength Section
    mbti_name_strength = models.CharField(max_length=100)
    pic_strength =models.URLField(blank=True, null=True)

    strength1 = models.CharField(max_length=100, blank=True, null=True)
    strength1_description = models.TextField(blank=True, null=True)

    strength2 = models.CharField(max_length=100, blank=True, null=True)
    strength2_description = models.TextField(blank=True, null=True)

    strength3 = models.CharField(max_length=100, blank=True, null=True)
    strength3_description = models.TextField(blank=True, null=True)

    strength4 = models.CharField(max_length=100, blank=True, null=True)
    strength4_description = models.TextField(blank=True, null=True)

    strength5 = models.CharField(max_length=100, blank=True, null=True)
    strength5_description = models.TextField(blank=True, null=True)

    strength6 = models.CharField(max_length=100, blank=True, null=True)
    strength6_description = models.TextField(blank=True, null=True)

    strength7 = models.CharField(max_length=100, blank=True, null=True)
    strength7_description = models.TextField(blank=True, null=True)

    strength8 = models.CharField(max_length=100, blank=True, null=True)
    strength8_description = models.TextField(blank=True, null=True)

    strength9 = models.CharField(max_length=100, blank=True, null=True)
    strength9_description = models.TextField(blank=True, null=True)

    strength10 = models.CharField(max_length=100, blank=True, null=True)
    strength10_description = models.TextField(blank=True, null=True)

    # Weakness Section
    mbti_name_weakness = models.CharField(max_length=100)
    pic_weakness = models.URLField(blank=True, null=True)

    weakness1 = models.CharField(max_length=100, blank=True, null=True)
    weakness1_description = models.TextField(blank=True, null=True)

    weakness2 = models.CharField(max_length=100, blank=True, null=True)
    weakness2_description = models.TextField(blank=True, null=True)

    weakness3 = models.CharField(max_length=100, blank=True, null=True)
    weakness3_description = models.TextField(blank=True, null=True)

    weakness4 = models.CharField(max_length=100, blank=True, null=True)
    weakness4_description = models.TextField(blank=True, null=True)

    weakness5 = models.CharField(max_length=100, blank=True, null=True)
    weakness5_description = models.TextField(blank=True, null=True)

    weakness6 = models.CharField(max_length=100, blank=True, null=True)
    weakness6_description = models.TextField(blank=True, null=True)

    weakness7 = models.CharField(max_length=100, blank=True, null=True)
    weakness7_description = models.TextField(blank=True, null=True)

    weakness8 = models.CharField(max_length=100, blank=True, null=True)
    weakness8_description = models.TextField(blank=True, null=True)

    weakness9 = models.CharField(max_length=100, blank=True, null=True)
    weakness9_description = models.TextField(blank=True, null=True)

    weakness10 = models.CharField(max_length=100, blank=True, null=True)
    weakness10_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.personality.code} - Strengths & Weaknesses"


#Relation content table

class RomanticRelationshipSection(models.Model):
    personality = models.OneToOneField(PersonalityType, on_delete=models.CASCADE, related_name='romantic_relationship')

    quote1 = models.TextField(blank=True, null=True)
    text1 = models.TextField()

    pic1 = models.URLField(blank=True, null=True)

    subheading1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)

    quote2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)

    pic2 = models.URLField(blank=True, null=True)

    subheading2 = models.CharField(max_length=255, blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)

    quote3 = models.TextField(blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)

    subheading3 = models.CharField(max_length=255, blank=True, null=True)
    text6 = models.TextField( blank=True, null=True)
    quote4 = models.TextField(blank=True, null=True)
    text7 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Romantic Relationship - {self.personality.code}"


class FriendshipSection(models.Model):
    personality = models.OneToOneField(
        PersonalityType,
        on_delete=models.CASCADE,
        related_name='friendship'
    )

    quote1 = models.TextField(blank=True, null=True)
    text1 = models.TextField()

    pic1 = models.URLField(blank=True, null=True)

    subheading1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)

    quote2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)

    subheading2 = models.CharField(max_length=255, blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)

    quote3 = models.TextField(blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Friendship - {self.personality.code}"


class ParenthoodSection(models.Model):
    personality = models.OneToOneField(PersonalityType, on_delete=models.CASCADE, related_name='parenthood')

    quote1 = models.TextField(blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    pic1 = models.URLField(blank=True, null=True)

    subheading1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)

    quote2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)

    subheading2 = models.CharField(max_length=255, blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)

    quote3 = models.TextField(blank=True, null=True)
    subheading3 = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Parenthood - {self.personality.code}"

class CareerPathSection(models.Model):
    personality = models.OneToOneField(PersonalityType, on_delete=models.CASCADE, related_name='career_path')

    quote1 = models.TextField(blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)

    quote2 = models.TextField(blank=True, null=True)
    pic1 = models.URLField(blank=True, null=True)

    subheading1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)

    quote3 = models.TextField(blank=True, null=True)
    subheading2 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)

    quote4 = models.TextField(blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)

    subheading3 = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)

    quote5 = models.TextField(blank=True, null=True)
    text6 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Career Path - {self.personality.code}"

class CareerOption(models.Model):
    career_path = models.ForeignKey(
        CareerPathSection,
        on_delete=models.CASCADE,
        related_name='career_options'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.career_path.personality.code}"


class WorkplaceHabitsSection(models.Model):
    personality = models.OneToOneField(
        PersonalityType,
        on_delete=models.CASCADE,
        related_name='workplace_habits'
    )

    text1 = models.TextField(blank=True, null=True)

    subheading1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)

    pic1 = models.URLField(blank=True, null=True)

    quote1 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)

    subheading2 = models.CharField(max_length=255, blank=True, null=True)
    text4 = models.TextField(blank=True, null=True)

    quote2 = models.TextField(blank=True, null=True)
    text5 = models.TextField(blank=True, null=True)

    subheading3 = models.CharField(max_length=255, blank=True, null=True)
    text6 = models.TextField(blank=True, null=True)

    quote3 = models.TextField(blank=True, null=True)
    text7 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Workplace Habits - {self.personality.code}"






from django.contrib import admin
from .models import (
    PersonalityType,
    IntroductionPage,
    RomanticRelationshipSection,
    StrengthWeaknessPage,
    FriendshipSection,
    ParenthoodSection,
    CareerPathSection,
    WorkplaceHabitsSection,
)

admin.site.register(PersonalityType)
admin.site.register(IntroductionPage)
admin.site.register(RomanticRelationshipSection)
admin.site.register(StrengthWeaknessPage)
admin.site.register(FriendshipSection)
admin.site.register(ParenthoodSection)
admin.site.register(CareerPathSection)
admin.site.register(CareerOption)
admin.site.register(WorkplaceHabitsSection)
