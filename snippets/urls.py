from django.urls import path
from .views import SnippetList, SnippetDetail, UserDetails, UserList
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('', views.api_root),
    path(''),
   # path('', views.snippet_list),
   # path('<int:pk>/', views.snippet_detail),
    path('', SnippetList.as_view()),
    path('<int:pk>/', SnippetDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetails.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)