import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_the_book_project.settings')

import django
django.setup()
from what_the_book.models import *
from datetime import date

def populate():
    
    users = [
        {
            'Username': 'John Dough',
            'Password': '1234567890'},
        {
            'Username': 'Jane Pastry',
            'Password': 'incorrect'},
        {
            'Username': 'ILOVEREADING3275',
            'Password': 'themostincrediblysecurepassword'},
    ]
    
    admins = [
        {
            'Username': 'theenforcer',
            'Password': 'password'},
        {
            'Username': 'big jim',
            'Password': 'xG8Wl*g6Fd'},
    ]
    
    books = [
        {
            'Title': 'Romeo and Juliet',
            'Author': 'William Shakespeare'},
        {
            'Title': 'Macbeth',
            'Author': 'William Shakespeare'},
        {
            'Title': 'Othello',
            'Author': 'William Shakespeare'},
        {
            'Title': 'King Lear',
            'Author': 'William Shakespeare'},

        


    ]
    
    requests = [
        {
            'Title': 'The Hobbit',
            'Author': 'J.R.R. Tolkien'},
        {
            'Title': 'The Very Hungry Caterpillar',
            'Author': 'Eric Carle'},
    ]
    
    reviews = [
        {
            'Title': 'lack of modernity',
            'MainText': 'a large body of text may be fit into a text field',
            'CreatedOn': date(2022, 3, 3),
            'Likes': 12},
        {
            'Title': 'macbeth? more like macsucks',
            'MainText': 'a deep and scathing review',
            'CreatedOn': date(2013, 7, 19),
            'Likes': 527},
    ]
    
        # Helper functions

    def add_user(Username, Password):
        user = User.objects.get_or_create(Username=Username, Password=Password)[0]
        user.save()
        return user
    
    def add_admin(Username, Password):
        admin = Admin.objects.get_or_create(Username=Username, Password=Password)[0]
        admin.save()
        return admin
    
    #Commented out code below is the original code for add_book, which was changed to the code below it
    """def add_book(AddedBy, Title, Author):
        book = Book.objects.get_or_create(Title=Title, Author=Author)[0]
        book.AddedBy=AddedBy
        book.save()
        return book"""
    
    def add_book(AddedBy, Title, Author):
        book = Book.objects.get_or_create(Title=Title, Author=Author, AddedBy=AddedBy)[0]
        book.save()
        return book
    
    def add_request(RequestedBy, ReadBy, Title, Author):
        request = BookToRequest.objects.get_or_create(Title=Title, Author=Author)[0]
        request.RequestedBy=RequestedBy
        request.ReadBy=ReadBy
        request.save()
        return request
    
    def add_review(ReviewOf, CreatedBy, Title, MainText, CreatedOn, Likes):
        review = Review.objects.get_or_create(Title=Title, MainText=MainText, CreatedOn=CreatedOn, Likes=Likes)[0]
        review.ReviewOf=ReviewOf
        review.CreatedBy=CreatedBy
        review.save()
        return review
    
    foreign_values = {
        'users': [],
        'admins': [],
        'books': [],
    }
    
    # Populate models
    
    for item in admins:
        admin = add_admin(**item)
        foreign_values['admins'].append(admin)
    
    for item in users:
        user = add_user(**item)
        foreign_values['users'].append(user)
    
    #Commented out code below is the original code for populating books, which was changed to the code below it
    """for index, item in enumerate(books):
        book = add_book(foreign_values['admins'][index], **item)
        foreign_values['books'].append(book)"""
    
    for index, item in enumerate(books):
        book = add_book(foreign_values['admins'][index % len(foreign_values['admins'])], **item)
        foreign_values['books'].append(book)

    
    for index, item in enumerate(requests):
        request = add_request(foreign_values['users'][index], foreign_values['admins'][index], **item)
    
    for index, item in enumerate(reviews):
        review = add_review(foreign_values['books'][index], foreign_values['users'][index], **item)
        
    # Print out population data

    print("\nUsers:")
    for user in User.objects.all():
        print(user)
        
    print("\nAdmins:")
    for admin in Admin.objects.all():
        print(admin)
        
    print("\nBooks:")
    for book in Book.objects.all():
        print(book)
        
    print("\nRequests")
    for request in BookToRequest.objects.all():
        print(request)
        
    print("\nReviews:")
    for review in Review.objects.all():
        print(review)

# Main

if __name__ == '__main__':
    print('Starting book population script...')
    populate()
