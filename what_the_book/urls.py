from django.urls import path
from what_the_book import views

app_name = 'what_the_book'

urlpatterns = [
    path('', views.home, name='home'),
    path('contactus/', views.contactus, name='contactus'),
    path('request_book/', views.request_book, name='request_book'),
    path('book/<slug:book_name_slug>', views.show_book, name='show_book' ),
    path('book/<slug:book_name_slug>/make_review/', views.make_review,name='make_review'),
]
