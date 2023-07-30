from django.urls import path
from .views import *
urlpatterns = [
    path('list/', MovieList.as_view(), name='movie_list'),
    path('detail/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
]
