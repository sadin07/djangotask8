from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.shortcuts import get_object_or_404
from .models import Book
from .models import Author
from django.db.models import Q


def home(request):
    return render(request, 'book/home.html')

def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book/bookdetail.html', {'book': book})


def author(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'book/authordetail.html', {'author': author})

def booklist(request):
    books = Book.objects.all() 
    return render(request, 'book/booklist.html', {'books': books})

def authorlist(request):
    authors = Author.objects.all() 
    return render(request, 'book/authorlist.html', {'authors': authors})

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
    return render(request, 'book/search.html', {'results': results, 'query': query})
