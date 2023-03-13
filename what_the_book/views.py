from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
from what_the_book.models import Book, Review,User,Admin
from what_the_book.forms import BookRequestForm,ReviewForm
from django.utils import timezone

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

def request_book(request):
    form = BookRequestForm()
    
    if request.method == 'POST':
        form = BookRequestForm()
        #save request to database
        if form.is_valid():
            form.save(commit=True)
            
            return redirect('/home/')
        else:
            print(form.errors)
           
       
    return render(request, 'what_the_book/request_book.html', {'form' :form})


def make_review(request,book_name_slug):

    try:
        reviewOf = Book.objects.get(slug = book_name_slug)

    except Book.DoesNotExist:
        reviewOf = None


    if reviewOf is None :
        return redirect('what_the_book')

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if reviewOf:
                review = form.save(commit= False)
                review.reviewOf = reviewOf

                review.likes = 0
                review.createdOn = timezone.now()
                review.save()

                return redirect(reverse('what_the_book:show_book', kwargs = {'book_name_slug':book_name_slug
                                                                            }))

            else:
                print(form.errors)

    context_dict = {'form':form,'reviewOf':reviewOf,}

    return render(request, 'what_the_book/make_review.html', context=context_dict)


            
            