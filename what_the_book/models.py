from django.db import models

class User(models.Model):
    UserId = models.AutoField(unique=True, primary_key=True)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    ProfilePicture = models.ImageField()
    
    def __str__(self):
        return f"{self.Username}"
    
class Admin(models.Model):
    UserId = models.AutoField(unique=True, primary_key=True)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    ProfilePicture = models.ImageField()
    
    def __str__(self):
        return f"{self.Username}"
    
class Book(models.Model):
    AddedBy = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=30)
    Author = models.CharField(max_length=20)
    CoverPicture = models.ImageField()
    
    def __str__(self):
        return f"{self.Title} by {self.Author}"
    
class BookToRequest(models.Model):
    RequestedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ReadBy = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=30)
    Author = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = 'Requested books'
    
    def __str__(self):
        return f"{self.Title} requested by {self.RequestedBy}"
    
class Review(models.Model):
    ReviewOf = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=30)
    MainText = models.TextField()
    CreatedOn = models.DateField()
    Likes = models.IntegerField(default=0)
        
    def __str__(self):
        return f"Review of {self.ReviewOf}  by {self.CreatedBy}"
    

