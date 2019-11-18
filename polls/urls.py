from django.urls import path
from .views import  question_list, detail, results, vote
from . import views


app_name = 'polls'
urlpatterns = [
    #/polls/
    #path("", question_list, name = 'list'),
    path("", views.ListView.as_view(), name='list'),
    #/polls/5/
    #path("<int:question_id>/", detail, name = 'detail'),
    #path("<int:question_id>/", detail, name = 'detail'),
    path("<int:pk>/", views.DetailView.as_view(), name = 'detail'),
    # /polls/5/results
    #path("<int:question_id>/results/", results, name = 'results'),
    path("<int:pk>/results", views.ResultView.as_view(), name = 'results'),
    #/polls/5/vote
    path("<int:question_id>/vote/", vote, name = 'vote'),
]