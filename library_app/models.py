from django.db import models
from django.core.validators import EmailValidator

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('hinduism', 'Hindu Scripture / Spiritual Philosophy'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class BorrowRecord(models.Model):
    user_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_name} - {self.book.title}"
    
    class Meta:
        ordering = ['-borrow_date']