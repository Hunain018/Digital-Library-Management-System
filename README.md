
Readme · MD
# 📚 Library Management System
 
A simple Library Management System built with **Python** and **Streamlit**, featuring a clean, custom-styled UI. Users can view, search, borrow, return, and add books through an interactive web interface.
 
## Features 
 
- 📖 **View Books** — See all books currently in the library with availability status
- 🔍 **Search Book** — Search by title or author
- 📥 **Borrow Book** — Borrow a book using its Book ID (reduces available copies)
- 📤 **Return Book** — Return a borrowed book (restores available copies)
- 🎒 **View My Borrowed Books** — See all books currently borrowed by the user
- ➕ **Add New Book** — Add new books to the library catalog
- 🎨 Custom dark-themed UI with styled book cards, gradient banners, and status badges
## Project Structure
 
```
library_app.py     # Main application file (models + Streamlit UI)
README.md          # Project documentation
```
 
## Tech Stack
 
- **Python 3**
- **Streamlit** — for the web interface
## How It Works
 
The app is built around three core classes:
 
- **`Book`** — stores title, author, book ID, total copies, and available copies
- **`User`** — stores user details and the list of books they've borrowed
- **`Library`** — manages the book catalog and handles adding, searching, borrowing, and returning books
Streamlit's `session_state` is used to persist the library and user data across interactions during a session.
 
## Installation
 
1. Make sure Python 3.8+ is installed.
2. Install Streamlit:
```bash
   pip install streamlit
```
 
## Running the App
 
From the project directory, run:
 
```bash
streamlit run library_app.py
```
 
This will open the app in your default browser at `http://localhost:8501`.
 
## Usage
 
1. Use the **sidebar menu** to navigate between features (View Books, Search Book, Borrow Book, etc.)
2. To **borrow** or **return** a book, enter the correct **Book ID** shown in the book listing.
3. To **add a new book**, fill in the title, author, book ID, and total copies, then click **Add Book**.
## Sample Data
 
On first run, the library is pre-loaded with:
 
| Book ID | Title                | Author  | Copies |
|---------|-----------------------|---------|--------|
| 1       | Python Basics          | Hunain  | 5      |
| 2       | Data Analysis Basics   | Basit   | 3      |
 
A default user **Hunain (ID: 101)** is created automatically.
 
## Notes / Limitations
 
- Data is stored only in the Streamlit session — it **resets when the app restarts** (no database or file persistence).
- Only one user session is simulated at a time (no login/multi-user system).
## Future Improvements
 
- Add persistent storage (SQLite / JSON file / database)
- Multi-user login system
- Book categories and filtering
- Due dates and overdue tracking
- 
