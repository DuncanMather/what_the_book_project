from datetime import datetime, timedelta
from django.test import TestCase
from what_the_book.models import *


class ModelTests(TestCase):
    def test_likes_non_negative(self):
        review = Review(title="Title", createdOn=datetime.now(), likes=-1)
        review.save()

        self.assertEqual((review.likes >= 0), True)

    def test_valid_date(self):
        review = Review(
            title="Title", createdOn=datetime.now() + timedelta(days=1))
        review.save()

        self.assertEqual((review.createdOn <= datetime.now()), True)

    def test_valid_book_slug(self):
        book = Book(title="A BOOK ABOUT SHOUTING")
        book.save()
        self.assertEqual((book.slug == "a-book-about-shouting"), True)
