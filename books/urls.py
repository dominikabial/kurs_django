from django.urls import path
from . import views
from .views import book_list, book_details


app_name = 'books'
urlpatterns = [
    #/polls/
    #path("", book_list, name = 'list'),
    path("", views.ListView.as_view(), name='list'),
    #path("<int:book_id>/", book_details, name = 'detail'),
    path("<int:pk>/", views.DetailView.as_view(), name = 'detail'),
]