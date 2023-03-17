from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from what_the_book.models import Book, Review, User, Admin
from what_the_book.forms import BookRequestForm, ReviewForm, UserForm, UserPictureForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def redirect_to_home(request):
    return redirect(reverse('what_the_book:home'))


def home(request):
    book_list = Book.objects.order_by('title')
    context_dict = {}
    context_dict['books'] = book_list
    return render(request, 'what_the_book/home.html', context=context_dict)


def contactus(request):
    return render(request, 'what_the_book/contactus.html', context={})


def show_book(request, book_title_slug):
    context_dict = {}
    try:
        book = Book.objects.get(
            Q(title__iexact=book_title_slug.replace('-', ' ')))
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
        # save request to database
        if form.is_valid():
            form.save(commit=True)

            return redirect('/home/')
        else:
            print(form.errors)

    return render(request, 'what_the_book/request_book.html', {'form': form})


def make_review(request, book_name_slug):

    try:
        reviewOf = Book.objects.get(slug=book_name_slug)

    except Book.DoesNotExist:
        reviewOf = None

    if reviewOf is None:
        return redirect('what_the_book')

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if reviewOf:
                review = form.save(commit=False)
                review.reviewOf = reviewOf

                review.likes = 0
                review.createdOn = timezone.now()
                review.save()

                return redirect(reverse('what_the_book:show_book', kwargs={'book_name_slug': book_name_slug
                                                                           }))

            else:
                print(form.errors)

    context_dict = {'form': form, 'reviewOf': reviewOf, }

    return render(request, 'what_the_book/make_review.html', context=context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_picture_form = UserPictureForm(request.POST)

        if user_form.is_valid() and user_picture_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            picture_user = user_picture_form.save(commit=False)
            picture_user.username = user_form['username'].value
            picture_user.password = user_form['password'].value

            if 'profilePicture' in request.FILES:
                picture_user.profilePicture = request.FILES['profilePicture']

            picture_user.save()
            registered = True
        else:
            print(user_form.errors, user_picture_form.errors)
    else:
        user_form = UserForm()
        user_picture_form = UserPictureForm()

    return render(request, 'what_the_book/register.html', context={'user_form': user_form,
                                                                   'user_picture_form': user_picture_form,
                                                                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect_to_home(request)
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, 'what_the_book/login.html')


@login_required
def account(request):
    return render(request, 'what_the_book/account.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect_to_home(request)
