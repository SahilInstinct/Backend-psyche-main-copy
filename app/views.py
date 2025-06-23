from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Question
from django.views.decorators.csrf import csrf_exempt
import json

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
            "Agree": (0.75, 0.25),
            "Neutral": (0.5, 0.5),
            "Disagree": (0.25, 0.75),
            "Strongly Disagree": (0.0, 1.0),
        }

        weight_map = {'Low': 1, 'Medium': 2, 'High': 3}

        for response in responses:
            q = Question.objects.get(id=response['question_id'])
            primary_letter = q.trait_if_agree[0]  # e.g., 'E'
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




@csrf_exempt
def save_result(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mbti = data.get('mbti')
        percentages = json.dumps(data.get('percentages'))
        request.user.profile.mbti_type = mbti
        request.user.profile.percentages = percentages
        request.user.profile.save()
        return JsonResponse({'message': 'Result saved!'})
    return None

