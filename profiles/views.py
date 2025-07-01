import json

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import Profile

from mbti_data.models import PersonalityType


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ✅ Ensure profile exists manually
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)

            return redirect('profile')  # or any success page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password. Please try again.'})

    return render(request, 'login.html', {})




def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists. Please choose another.'
            })

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # log them in right after register
        return redirect('home')  # or wherever you want to go

    return render(request,'register.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    mbti = profile.mbti_type  # e.g., INTJ-T
    base_code = mbti.split('-')[0]  # Remove identity suffix

    percentages = {
        'Mind': {
            'Introversion': profile.mind_introversion,
            'Extraversion': profile.mind_extraversion
        },
        'Energy': {
            'Intuition': profile.energy_intuition,
            'Sensing': profile.energy_sensing
        },
        'Nature': {
            'Thinking': profile.nature_thinking,
            'Feeling': profile.nature_feeling
        },
        'Tactics': {
            'Judging': profile.tactics_judging,
            'Prospecting': profile.tactics_prospecting
        },
        'Identity': {
            'Assertive': profile.identity_assertive,
            'Turbulent': profile.identity_turbulent
        }
    }

    try:
        personality = PersonalityType.objects.get(code=base_code)
    except PersonalityType.DoesNotExist:
        personality = None

    return render(request, "profile.html", {
        "mbti": mbti,
        "mbti_code": base_code,
        "percentages": percentages,
        "personality_name": personality.name if personality else "Unknown",
        "personality_description": personality.description if personality else "",
        "hero_image": personality.hero_image if personality else "",
    })

