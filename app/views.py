from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Question
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from profiles.models import Profile

# Create your views here.

def homePageView(req):
    return render(req, "home.html")

def testPageView(req):
    return render(req, "test.html")

def get_questions(request):
    questions = Question.objects.all().order_by('id')
    data = []

    for q in questions:
        data.append({
            'id': q.id,
            'text': q.question_text,
            'aspect': q.aspect,
            'trait': q.trait_if_agree,
            'weight': q.weight
        })

    return JsonResponse({'questions': data})

@csrf_exempt
def submit_answers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        responses = data.get('responses', [])

        traits = {
            'I': 0, 'E': 0,
            'S': 0, 'N': 0,
            'T': 0, 'F': 0,
            'J': 0, 'P': 0,
            'A': 0, 'B': 0,  # B for Turbulent
        }

        response_weights = {
            "Strongly Agree": (1.0, 0.0),
            "Agree": (0.8, 0.2),
            "Neutral": (0.2, 0.2),
            "Disagree": (0.2, 0.8),
            "Strongly Disagree": (0.0, 1.0),
        }

        weight_map = {'Low': 1, 'Medium': 1.5, 'High': 2}

        trait_map = {
            "Introversion": "I", "Extraversion": "E",
            "Sensing": "S", "Intuition": "N",
            "Thinking": "T", "Feeling": "F",
            "Judging": "J", "Prospecting": "P",
            "Assertive": "A", "Turbulent": "B"
        }

        for response in responses:
            q = Question.objects.get(id=response['question_id'])


            trait_name = q.trait_if_agree.strip()
            if trait_name not in trait_map:
                raise ValueError(f"Unknown trait in question ID {q.id}: '{trait_name}'")

            primary_letter = trait_map[trait_name]
            opposite_letter = get_opposite(primary_letter)

            primary_score, opposite_score = response_weights[response['answer']]
            weight = weight_map.get(q.weight, 2)

            traits[primary_letter] += primary_score * weight
            traits[opposite_letter] += opposite_score * weight


        mbti = ''.join([
            'E' if traits['E'] >= traits['I'] else 'I',
            'N' if traits['N'] >= traits['S'] else 'S',
            'F' if traits['F'] >= traits['T'] else 'T',
            'J' if traits['J'] >= traits['P'] else 'P'
        ])
        identity = 'A' if traits['A'] >= traits['B'] else 'T'



        percentages = {
            'Mind': {
                'Introversion': round(traits['I'] / (traits['I'] + traits['E']) * 100, 2),
                'Extraversion': round(traits['E'] / (traits['I'] + traits['E']) * 100, 2),
            },
            'Energy': {
                'Sensing': round(traits['S'] / (traits['S'] + traits['N']) * 100, 2),
                'Intuition': round(traits['N'] / (traits['S'] + traits['N']) * 100, 2),
            },
            'Nature': {
                'Thinking': round(traits['T'] / (traits['T'] + traits['F']) * 100, 2),
                'Feeling': round(traits['F'] / (traits['T'] + traits['F']) * 100, 2),
            },
            'Tactics': {
                'Judging': round(traits['J'] / (traits['J'] + traits['P']) * 100, 2),
                'Prospecting': round(traits['P'] / (traits['J'] + traits['P']) * 100, 2),
            },
            'Identity': {
                'Assertive': round(traits['A'] / (traits['A'] + traits['B']) * 100, 2),
                'Turbulent': round(traits['B'] / (traits['A'] + traits['B']) * 100, 2),
            }
        }

        return JsonResponse({'mbti': mbti + '-' + identity, 'percentages': percentages})

    return None

def get_opposite(trait_char):
    return {
        'I': 'E', 'E': 'I',
        'S': 'N', 'N': 'S',
        'T': 'F', 'F': 'T',
        'J': 'P', 'P': 'J',
        'A': 'B', 'B': 'A',
    }.get(trait_char, trait_char)





from profiles.models import Profile

@csrf_exempt  # frontend already sends CSRF, but keep this to avoid conflict
@require_POST
def save_result(request):
    try:
        data = json.loads(request.body)
        mbti = data.get('mbti')
        percentages = data.get('percentages', {})

        # get or create profile
        profile, created = Profile.objects.get_or_create(user=request.user)

        # Extract mbti_code from mbti_type
        if "-" in mbti:
            mbti_code = mbti.split("-")[0]  # "INTJ"
        else:
            mbti_code = mbti  # fallback in case no dash

        profile.mbti_type = mbti  # "INTJ-A"
        profile.mbti_code = mbti_code

        # Feed aspect values individually
        profile.mind_introversion = percentages.get("Mind", {}).get("Introversion", 0)
        profile.mind_extraversion = percentages.get("Mind", {}).get("Extraversion", 0)

        profile.energy_intuition = percentages.get("Energy", {}).get("Intuition", 0)
        profile.energy_sensing = percentages.get("Energy", {}).get("Sensing", 0)

        profile.nature_thinking = percentages.get("Nature", {}).get("Thinking", 0)
        profile.nature_feeling = percentages.get("Nature", {}).get("Feeling", 0)

        profile.tactics_judging = percentages.get("Tactics", {}).get("Judging", 0)
        profile.tactics_prospecting = percentages.get("Tactics", {}).get("Prospecting", 0)

        profile.identity_assertive = percentages.get("Identity", {}).get("Assertive", 0)
        profile.identity_turbulent = percentages.get("Identity", {}).get("Turbulent", 0)

        profile.save()

        return JsonResponse({"status": "success"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

def aboutPageView(req):
    return render(req, "about.html")