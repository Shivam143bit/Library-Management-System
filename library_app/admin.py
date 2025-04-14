from django.contrib import admin
from .models import Author, Book, BorrowRecord

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'published_date', 'author', 'created_at')
    list_filter = ('genre', 'published_date', 'author')
    search_fields = ('title', 'author__name')
    autocomplete_fields = ('author',)

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'book', 'borrow_date', 'return_date', 'created_at')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user_name', 'book__title')
    autocomplete_fields = ('book',)