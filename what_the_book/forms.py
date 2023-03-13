from django import forms 
from what_the_book.models import BookToRequest, Review


class BookRequestForm(forms.ModelForm):
    
    #entries for title and author. I have excluded some fields as they are specified in the models
    title = forms.CharField(max_length = 128,
                            help_text = "Please enter the title of the Book you would like to add")
    author = forms.CharField(max_length = 128,
                            help_text = "Please enter the author of the Book you would like to add")

    



    class Meta:
        #specifies related model
        model = BookToRequest
        
        #fields specifies which fields are included on the form 
        fields = ('title','author')
    

class ReviewForm(forms.ModelForm):
    
    #entries for title and maintext 
    
    title =  forms.CharField(max_length = 128,
                            help_text = "Please enter title for review")
    
    mainText  =  forms.CharField(max_length = 4000,
                            help_text = "Please write your review")
    


    class Meta:
        
        #specifies relevant model and which fields are included
        
        model = Review
        
        fields = ('title','mainText')
        
    
    
    
    
    