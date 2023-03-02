from django.urls import path
from what_the_book import views

app_name = 'what_the_book'

urlpatterns = [
    path('', views.home, name='home'),
    path('contactus/', views.contact_us, name='contact_us'),
]
