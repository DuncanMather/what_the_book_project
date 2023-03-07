from django.shortcuts import render, redirect
from django.http import HttpResponse
from what_the_book.models import Book

def redirect_to_home(request):
    response = redirect('home/')
    return response

def home(request):
    book_list = Book.objects.order_by('Title')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Just some random text'
    context_dict['books'] = book_list
    return render(request, 'what_the_book/home.html', context = context_dict)

def contactus(request):
    return render(request, 'what_the_book/contactus.html', context = {})