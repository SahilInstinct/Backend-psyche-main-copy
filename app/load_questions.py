import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Question #here replace the table name if ever wanted to add anything in the future

# add the list with tuple element such that it contains all the column data you wants to add

'''
for reference there is how you can update in the DB 

for question_text, aspect, trait, weight in mbti_questions:
    Question.objects.create(
        question_text = question_text,
        aspect = aspect,
        trait_if_agree = trait,
        weight = weight
    )
'''
from mbti_data.models import PersonalityType, Compatibility

intj = PersonalityType.objects.get(code="INTJ")
Compatibility.objects.create(
    personality=intj,
    romance_matches="ENFP,INFP,ENTP",
    friendship_matches="INFJ,INTP,ISTJ",
    career_matches="ENTJ,ISTP,ESTJ"
)



print("✅ Loaded into DB")

