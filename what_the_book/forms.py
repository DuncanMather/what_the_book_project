from django import forms
from what_the_book.models import BookToRequest, Review
from what_the_book.models import User as UserPicture
from django.contrib.auth.models import User


class BookRequestForm(forms.ModelForm):

    # entries for title and author. I have excluded some fields as they are specified in the models
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the Book you would like to add")
    author = forms.CharField(max_length=128,
                             help_text="Please enter the author of the Book you would like to add")

    class Meta:
        # specifies related model
        model = BookToRequest

        # fields specifies which fields are included on the form
        fields = ('title', 'author')


class ReviewForm(forms.ModelForm):

    # entries for title and maintext

    title = forms.CharField(max_length=128,
                            help_text="Please enter title for review")

    mainText = forms.CharField(max_length=4000,
                               help_text="Please write your review")

    class Meta:

        # specifies relevant model and which fields are included

        model = Review

        fields = ('title', 'mainText')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserPictureForm(forms.ModelForm):
    class Meta:
        model = UserPicture
        fields = ('profilePicture',)
