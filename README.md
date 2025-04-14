# Django Library Management System

A Django web application to manage an online library system where admins can manage books, authors, and their borrow records.

## Features

- Manage authors, books, and borrow records
- Form validation
- Pagination
- Export data to Excel
- Responsive UI with Bootstrap

### Project Setup
  - Create a virtual environment and activate it:
      python -m venv venv
      venv\Scripts\activate
    
  - Install the required packages:
      pip install -r requirements.txt

  - Run migrations:
      python manage.py makemigrations
      python manage.py migrate

  - Create a superuser (admin):
      python manage.py createsuperuser

  - Run server:
      python manage.py runserver  //Access the application at [http://127.0.0.1:8000/]
    



