from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


from django.views.generic import DetailView, ListView,View
from .models import Books


class SearchBooksView(ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


#get id
class BooksDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'
    context_object_name = 'books_id'

    def get_object(self):
        return get_object_or_404(Books, id=self.kwargs['id'])


class BooksListView(ListView):
    model = Books
    template_name = 'book.html'
    context_object_name = 'query'

class AboutMeView(View):
    def get(self, request):
        return HttpResponse("My name is Amir")

class DomesticView(View):
    def get(self, request):
        html_content = """
        <html>
            <body>
                <h1>Bobik</h1>
                <img src="https://upload.wikimedia.org/wikipedia/ru/b/ba/%D0%90%D0%BA%D1%80%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D1%82.jpg" alt="Image" />
            </body>
        </html>
        """
        return HttpResponse(html_content)

class TimeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f"{datetime.now()}")