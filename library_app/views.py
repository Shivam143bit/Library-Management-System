from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Author, Book, BorrowRecord
from .forms import AuthorForm, BookForm, BorrowRecordForm
import xlsxwriter
from io import BytesIO

# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'library_app/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library_app/author_form.html'
    success_url = reverse_lazy('author-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Author added successfully!')
        return super().form_valid(form)

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library_app/author_form.html'
    success_url = reverse_lazy('author-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Author updated successfully!')
        return super().form_valid(form)
    

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
    template_name = 'library_app/confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'author'
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Author deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'library_app/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library_app/book_form.html'
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Book added successfully!')
        return super().form_valid(form)

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library_app/book_form.html'
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'library_app/confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'book'
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Book deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Borrow Record Views
class BorrowRecordListView(ListView):
    model = BorrowRecord
    template_name = 'library_app/borrow_list.html'
    context_object_name = 'borrow_records'
    paginate_by = 10

class BorrowRecordCreateView(CreateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library_app/borrow_form.html'
    success_url = reverse_lazy('borrow-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Borrow record added successfully!')
        return super().form_valid(form)

class BorrowRecordUpdateView(UpdateView):
    model = BorrowRecord
    form_class = BorrowRecordForm
    template_name = 'library_app/borrow_form.html'
    success_url = reverse_lazy('borrow-list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Borrow record updated successfully!')
        return super().form_valid(form)

class BorrowRecordDeleteView(DeleteView):
    model = BorrowRecord
    success_url = reverse_lazy('borrow-list')
    template_name = 'library_app/confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'borrow'
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Borrow record deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Export to Excel
def export_library_data(request):
    try:
        # Create an in-memory output file for the Excel workbook
        output = BytesIO()
        
        # Create a workbook and add worksheets
        workbook = xlsxwriter.Workbook(output)
        author_sheet = workbook.add_worksheet('Authors')
        book_sheet = workbook.add_worksheet('Books')
        borrow_sheet = workbook.add_worksheet('Borrow Records')
        
        # Add a bold format to use to highlight cells
        bold = workbook.add_format({'bold': True})
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
        
        # Write headers for Author sheet
        author_sheet.write(0, 0, 'ID', bold)
        author_sheet.write(0, 1, 'Name', bold)
        author_sheet.write(0, 2, 'Email', bold)
        author_sheet.write(0, 3, 'Bio', bold)
        
        # Write Author data
        authors = Author.objects.all()
        for row_num, author in enumerate(authors, 1):
            author_sheet.write(row_num, 0, author.id)
            author_sheet.write(row_num, 1, author.name)
            author_sheet.write(row_num, 2, author.email)
            author_sheet.write(row_num, 3, author.bio)
        
        # Write headers for Book sheet
        book_sheet.write(0, 0, 'ID', bold)
        book_sheet.write(0, 1, 'Title', bold)
        book_sheet.write(0, 2, 'Genre', bold)
        book_sheet.write(0, 3, 'Published Date', bold)
        book_sheet.write(0, 4, 'Author', bold)
        
        # Write Book data
        books = Book.objects.all()
        for row_num, book in enumerate(books, 1):
            book_sheet.write(row_num, 0, book.id)
            book_sheet.write(row_num, 1, book.title)
            book_sheet.write(row_num, 2, book.get_genre_display())
            book_sheet.write_datetime(row_num, 3, book.published_date, date_format)
            book_sheet.write(row_num, 4, book.author.name)
        
        # Write headers for Borrow Record sheet
        borrow_sheet.write(0, 0, 'ID', bold)
        borrow_sheet.write(0, 1, 'User Name', bold)
        borrow_sheet.write(0, 2, 'Book', bold)
        borrow_sheet.write(0, 3, 'Borrow Date', bold)
        borrow_sheet.write(0, 4, 'Return Date', bold)
        
        # Write Borrow Record data
        borrow_records = BorrowRecord.objects.all()
        for row_num, record in enumerate(borrow_records, 1):
            borrow_sheet.write(row_num, 0, record.id)
            borrow_sheet.write(row_num, 1, record.user_name)
            borrow_sheet.write(row_num, 2, record.book.title)
            borrow_sheet.write_datetime(row_num, 3, record.borrow_date, date_format)
            if record.return_date:
                borrow_sheet.write_datetime(row_num, 4, record.return_date, date_format)
        
        # Close the workbook
        workbook.close()
        
        # Seek to the beginning of the stream
        output.seek(0)
        
        # Create the HttpResponse with the appropriate Excel headers
        response = HttpResponse(
            output.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'
        
        messages.success(request, 'Data exported successfully!')
        return response
    except Exception as e:
        messages.error(request, f'Error exporting data: {str(e)}')
        return redirect('book-list')