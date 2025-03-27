from django.urls import path
from . import views

urlpatterns = [
    path("about_me/", views.AboutMeView.as_view(), name="about_me"),
    path("domestic/", views.DomesticView.as_view(), name="domestic"),
    path("time/", views.TimeView.as_view(), name="time"),
    path('', views.BooksListView.as_view(),name='books'),
    path('books_list/<int:id>/', views.BooksDetailView.as_view()),
    path('search/',views.SearchBooksView.as_view(),name='search'),
]