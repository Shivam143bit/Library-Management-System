from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Book, BorrowRecord

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith(('.com', '.org', '.edu', '.net')):
            raise ValidationError('Please enter a valid email domain.')
        return email

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all().order_by('name')

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
            'borrow_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all().order_by('title')
    
    def clean(self):
        cleaned_data = super().clean()
        borrow_date = cleaned_data.get('borrow_date')
        return_date = cleaned_data.get('return_date')
        
        if borrow_date and return_date and return_date < borrow_date:
            raise ValidationError('Return date cannot be earlier than borrow date.')
        
        return cleaned_data