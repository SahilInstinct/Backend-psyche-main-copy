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
        "personality": personality
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
    })

def show_friendship(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    friendship = getattr(personality, 'friendship', None)

    return render(request, 'mbti/friendship.html', {
        'personality': personality,
        'friendship': friendship
    })

def show_parenthood(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    parenthood = getattr(personality, 'parenthood', None)

    return render(request, 'mbti/parenthood.html', {
        'personality': personality,
        'parenthood': parenthood,
    })

def show_career_path(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    career = getattr(personality, 'career_path', None)

    return render(request, 'mbti/career.html', {
        'personality': personality,
        'career': career
    })

def show_workplace_habits(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    workplace = getattr(personality, 'workplace_habits', None)

    return render(request, 'mbti/workplace.html', {
        'personality': personality,
        'workplace': workplace
    })

def show_conclusion(request, code):
    personality = get_object_or_404(PersonalityType, code=code.upper())
    conclusion = getattr(personality, 'conclusion', None)

    return render(request, 'mbti/conclusion.html', {
        'personality': personality,
        'conclusion': conclusion
    })