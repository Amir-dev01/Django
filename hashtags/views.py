from django.shortcuts import render
from . import models


def all_category_film(request):
    if request.method == 'GET':
        query = models.Post.objects.all()
        return render(request,
                      template_name='tags/all_category_books.html',
                      context={'query': query}
                      )
def teen_category_film(request):
    if request.method == 'GET':
        query = models.Post.objects.all().filter(tags__name='Книги для подростков')
        return render(request,
                      template_name='tags/teen_category_film.html',
                      context={'query': query}
                      )
def kids_category_film(request):
    if request.method == 'GET':
        query = models.Post.objects.all().filter(tags__name='Книги для детей')
        return render(request,
                      template_name='tags/kids_category_film.html',
                      context={'query': query})