# 📚 Library Management System

   A Django-based web application for managing books, authors, and borrow records in a library.

---

## 🔧 Features

   - Add, update, delete authors and books.
   - Track borrowed books and their return status.
   - Pagination for long lists.
   - Form validation with user-friendly UI.
   - Export functionality (Excel, CSV) *(optional feature)*

---

## 🚀 Getting Started

   Follow these steps to set up and run the project locally.

---
## 🧰 Prerequisites

   Make sure you have the following installed:

   - Python 3.8+
   - pip
   - virtualenv *(recommended)*



## ⚙️ Installation

1. **Clone the Repository**
   
   git clone https://github.com/your-username/library-management.git

   cd library-management

2. **Create Virtual Environment**

   python -m venv venv

   source venv/bin/activate      (On Windows: venv\Scripts\activate)

3. **Install Dependencies**

   pip install -r requirements.txt

4. **Apply Migrations**

   python manage.py makemigrations

   python manage.py migrate

5. **Create Superuser (Optional for Admin Access)**

   python manage.py createsuperuser

6. **Run the Development Server**

   python manage.py runserver

7. **Access in Browser**

   Visit: http://127.0.0.1:8000/

   Admin: http://127.0.0.1:8000/admin/

## 🗃️ Admin Credentials (if created)

   Username	    -->   admin	   

   Password     -->   admin123 (example)

## 🛠 Technologies Used

i) Django

ii) SQLite (default DB)

iii) Bootstrap (for UI)
