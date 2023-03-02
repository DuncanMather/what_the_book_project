from django.shortcuts import render, redirect
from django.http import HttpResponse

def redirect_to_home(request):
    response = redirect('home/')
    return response

def home(request):
    return HttpResponse("<a href='/home/contactus/'>Contact us.</a>")

def contact_us(request):
    return HttpResponse("<a href='/home/'>Home.</a>")