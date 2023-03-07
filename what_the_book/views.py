from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from what_the_book.models import Book, Review
def redirect_to_home(request):
    response = redirect('home/')
    return response

def home(request):
    book_list = Book.objects.order_by('title')
    context_dict = {}
    context_dict['books'] = book_list
    return render(request, 'what_the_book/home.html', context=context_dict)

def contactus(request):
    return render(request, 'what_the_book/contactus.html', context = {})

def show_book(request, book_title_slug):
    context_dict = {}
    try:
        book = Book.objects.get(Q(title__iexact=book_title_slug.replace('-', ' ')))
        reviews = Review.objects.filter(reviewOf=book)
    except Book.DoesNotExist:
        book = None
        reviews = Review.objects.none()
    
    context_dict['book'] = book
    context_dict['reviews'] = reviews
    return render(request, 'what_the_book/book.html', context_dict)
