from .views import homePageView, testPageView, get_questions, submit_answers, save_result, aboutPageView
from django.urls import path


urlpatterns = [
path("", homePageView, name="home"),
path("testpage/", testPageView, name="test"),
path('get-questions/', get_questions, name='get_questions'),
path('submit-answers/', submit_answers, name='submit_answers'),
path('save-result/', save_result, name='save_result'),
path("about/", aboutPageView, name="about"),



]
