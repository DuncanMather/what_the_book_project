from django.shortcuts import render, redirect
from django.http import HttpResponse

def redirect_to_home(request):
    response = redirect('home/')
    return response

def home(request):
    context_dict = {'boldmessage': 'Template variable!'}
    return render(request, 'what_the_book/home.html', context = context_dict)

def contactus(request):
    return render(request, 'what_the_book/contactus.html', context = {})