from django.shortcuts import render
from django.http import HttpResponse
from .models import Author


# Create your views here.

def welcome(request):
    return HttpResponse('ok')


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'book/author-list.html', {'authors': authors})
