from django.shortcuts import render, get_object_or_404
from .models import PersonalityType

# Explore page that shows all MBTI cards
def explore_grid(request):
    personality_types = PersonalityType.objects.all()
    return render(request, "explore.html", {
        "personality_types": personality_types
    })


# Introduction section page
def show_introduction(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    return render(request, "mbti/introduction.html", {
        "personality": personality,
        'active_tab': 'intro',
    })

def show_strength_weakness(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    strength = getattr(personality, 'strength_weakness_page', None)

    return render(request, 'mbti/strength_weakness.html', {
        'personality': personality,
        'strength': strength,
        'active_tab': 'strength',
    })

def show_relationship(request, code):
    # Get the MBTI type
    personality = get_object_or_404(PersonalityType, code=code.upper())

    # Get the Romantic Relationship Section
    relationship = getattr(personality, 'romantic_relationship', None)

    # Render the template
    return render(request, 'mbti/relationship.html', {
        'personality': personality,
        'relationship': relationship,
        'active_tab': 'relationship',
    })

def show_friendship(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    friendship = getattr(personality, 'friendship', None)

    return render(request, 'mbti/friendship.html', {
        'personality': personality,
        'friendship': friendship,
        'active_tab': 'friend',
    })

def show_parenthood(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    parenthood = getattr(personality, 'parenthood', None)

    return render(request, 'mbti/parenthood.html', {
        'personality': personality,
        'parenthood': parenthood,
        'active_tab': 'parent',
    })

def show_career_path(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    career = getattr(personality, 'career_path', None)

    return render(request, 'mbti/career.html', {
        'personality': personality,
        'career': career,
        'active_tab': 'career',
    })

def show_workplace_habits(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    workplace = getattr(personality, 'workplace_habits', None)

    return render(request, 'mbti/workplace.html', {
        'personality': personality,
        'workplace': workplace,
        'active_tab': 'work',
    })

def compatibility_page(request):
    return render(request, "compatibility.html")

def book_recommendation(request):
    return render(request, "book_recommendation.html")

def famous_mbti_page(request):
    return render(request, "famous_mbti.html")