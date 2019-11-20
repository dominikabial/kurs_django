from django.urls import path
from . import views
from .views import book_list, book_details, book_comment, books_to_excel

from django.contrib.auth.decorators import login_required


app_name = 'books'
urlpatterns = [
    #/polls/
    path("", book_list, name = 'list'),
    # path("", views.ListView.as_view(), name='list'),
    path("report/", books_to_excel, name='report'),
    #path("<int:book_id>/", book_details, name = 'detail'),
    path("<int:pk>/", login_required(views.DetailView.as_view()), name='detail'),
    path("<int:pk>/comment", book_comment, name='comment')
]