from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_films/', views.all_category_film, name='all'),
    path('teen_hashtags_films/', views.teen_category_film, name='teen'),
    path('kids_hashtags_films/', views.kids_category_film, name='kids'),
]