from django.contrib import admin
from what_the_book.models import *

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Book)
admin.site.register(BookToRequest)
admin.site.register(Review)

