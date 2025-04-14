from django.urls import path
from . import views

urlpatterns = [
    # Author URLs
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='author-add'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author-edit'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    
    # Book URLs
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/add/', views.BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    
    # Borrow Record URLs
    path('borrows/', views.BorrowRecordListView.as_view(), name='borrow-list'),
    path('borrows/add/', views.BorrowRecordCreateView.as_view(), name='borrow-add'),
    path('borrows/<int:pk>/edit/', views.BorrowRecordUpdateView.as_view(), name='borrow-edit'),
    path('borrows/<int:pk>/delete/', views.BorrowRecordDeleteView.as_view(), name='borrow-delete'),
    

    
    # Export URL
    path('export/', views.export_library_data, name='export-data'),
]