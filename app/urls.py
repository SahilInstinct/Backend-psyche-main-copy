from .views import homePageView, testPageView,get_questions, submit_answers, chatbot_response
from django.urls import path
from . import views


urlpatterns = [
path("", homePageView, name="home"),
path("testpage/", testPageView, name="test"),
path('get-questions/', get_questions, name='get_questions'),
path('submit-answers/', submit_answers, name='submit_answers'),
path("chatbot/", chatbot_response, name="chatbot_response"),

]
