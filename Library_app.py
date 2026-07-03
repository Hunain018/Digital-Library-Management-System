import streamlit as st

# --------------------- Page Config ---------------------

st.set_page_config(page_title="Library Management System", page_icon="📚", layout="wide")

# --------------------- Book Class ---------------------

class Book:
    def __init__(self, title, author, book_id, total_copies):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def display(self):
        return f"{self.book_id} | {self.title} by {self.author} | Available: {self.available_copies}/{self.total_copies}"

# --------------------- User Class ---------------------

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
             self.borrowed_books.remove(book)

    def view_borrowed_books(self):
        return [ book.display() for book in self.borrowed_books] if self.borrowed_books else ["No borrowed books"]

# --------------------- Library Class ---------------------

class Library:
    def __init__(self):
        self.books = []
       
    def add_books(self, book):
        self.books.append(book)
    
    def view_books(self):
        return [book.display() for book in self.books] if self.books else ["No books in library"]

    
    def search_book(self, title):
         return[book.display() for book in self.books if book.title.lower() == title.lower()]

    def search_book_author(self, author):
         return [book.display() for book in self.books if book.author.lower() == author.lower()]
    
    def borrow_book(self, user, book_id):
         for book in self.books:
              if book.book_id == book_id:
                if book.available_copies > 0:
                   book.available_copies -= 1
                   user.borrow_book(book)
                   return f"'{book.title}' is borrowed"
                else:
                     return "Book not available"
         return "Book not found"
    
    def return_book(self, user, book_id):
         for book in user.borrowed_books:
              if book.book_id == book_id:
                 book.available_copies += 1
                 user.borrowed_books.remove(book)
                 return f"'{book.title}' is returned"
         return "Book is unavailable"

# --------------------- Custom CSS ---------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #4338ca 0%, #6d28d9 100%);
}
section[data-testid="stSidebar"] * {
    color: #f5f3ff !important;
}
section[data-testid="stSidebar"] label {
    font-weight: 600;
}

/* Main title banner */
.main-title {
    background: linear-gradient(90deg, #6366f1, #a855f7);
    padding: 28px 32px;
    border-radius: 16px;
    margin-bottom: 28px;
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.35);
}
.main-title h1 {
    color: white;
    margin: 0;
    font-weight: 700;
    font-size: 34px;
}
.main-title p {
    color: #ede9fe;
    margin: 4px 0 0 0;
    font-size: 15px;
}

/* Section subheaders */
.section-header {
    color: #f9fafb;
    font-weight: 600;
    font-size: 22px;
    margin: 10px 0 18px 0;
    padding-bottom: 8px;
    border-bottom: 2px solid #6366f1;
}

/* Book card */
.book-card {
    background: #1f2937;
    border: 1px solid #374151;
    border-left: 5px solid #6366f1;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    transition: transform 0.15s ease;
}
.book-card:hover {
    transform: translateY(-2px);
    border-left-color: #a855f7;
}
.book-card .book-title {
    color: #f9fafb;
    font-weight: 600;
    font-size: 17px;
}
.book-card .book-meta {
    color: #9ca3af;
    font-size: 14px;
    margin-top: 4px;
}
.book-card .badge {
    display: inline-block;
    margin-top: 8px;
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}
.badge-available {
    background: #064e3b;
    color: #6ee7b7;
}
.badge-unavailable {
    background: #7f1d1d;
    color: #fca5a5;
}

/* Empty state */
.empty-state {
    color: #9ca3af;
    font-style: italic;
    padding: 20px;
    text-align: center;
    border: 1px dashed #4b5563;
    border-radius: 12px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #6366f1, #a855f7);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 22px;
    font-weight: 600;
    transition: opacity 0.15s ease;
}
.stButton > button:hover {
    opacity: 0.9;
    color: white;
}

/* Inputs */
div[data-baseweb="input"], div[data-baseweb="select"] {
    border-radius: 10px !important;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# --------------------- Helper: render a book card ---------------------

def render_book_card(book: Book):
    badge_class = "badge-available" if book.available_copies > 0 else "badge-unavailable"
    badge_text = "Available" if book.available_copies > 0 else "Out of stock"
    st.markdown(f"""
    <div class="book-card">
        <div class="book-title">📖 {book.title}</div>
        <div class="book-meta">by {book.author} &nbsp;•&nbsp; ID: {book.book_id} &nbsp;•&nbsp; Copies: {book.available_copies}/{book.total_copies}</div>
        <span class="badge {badge_class}">{badge_text}</span>
    </div>
    """, unsafe_allow_html=True)

def render_empty(message):
    st.markdown(f'<div class="empty-state">{message}</div>', unsafe_allow_html=True)

# ---------------------   Title   ---------------------

st.markdown("""
<div class="main-title">
    <h1>📚 Library Management System</h1>
    <p>Browse, search, borrow and manage your books with ease</p>
</div>
""", unsafe_allow_html=True)

# Maintain state
if "library" not in st.session_state:
    st.session_state.library = Library()
if "user" not in st.session_state:
    st.session_state.user = User("Hunain", 101)

library = st.session_state.library
user = st.session_state.user

# Sample books (initial data)
if "initialized" not in st.session_state:
    book1 = Book("Python Basics", "Hunain", 1, 5)
    book2 = Book("Data Analysis Basics", "Basit", 2, 3)
    library.add_books(book1)
    library.add_books(book2)
    st.session_state.initialized = True

# --------------------- Sidebar Menu ---------------------

st.sidebar.markdown("### 🧭 Navigation")
menu = st.sidebar.selectbox("Menu", ["View Books", "Search Book", "Borrow Book", "Return Book", "View My Borrowed Books", "Add New Book"])

# --------------------- Menu Function ---------------------

if menu == "View Books":
    st.markdown('<div class="section-header">📚 All Books in Library</div>', unsafe_allow_html=True)
    if library.books:
        for book in library.books:
            render_book_card(book)
    else:
        render_empty("No books in library")

elif menu == "Search Book":
    st.markdown('<div class="section-header">🔍 Search for a Book</div>', unsafe_allow_html=True)
    option = st.radio("Search By:", ["Title", "Author"], horizontal=True)
    query = st.text_input("Enter search query:")
    if st.button("Search"):
        if option == "Title":
            results = [b for b in library.books if b.title.lower() == query.lower()]
        else:
            results = [b for b in library.books if b.author.lower() == query.lower()]
        if results:
            for b in results:
                render_book_card(b)
        else:
            render_empty("No matching books found")

elif menu == "Borrow Book":
    st.markdown('<div class="section-header">📥 Borrow a Book</div>', unsafe_allow_html=True)
    book_id = st.number_input("Enter Book ID to borrow:", min_value=1, step=1)
    if st.button("Borrow"):
        msg = library.borrow_book(user, book_id)
        if "borrowed" in msg:
            st.success(msg)
        else:
            st.warning(msg)

elif menu == "Return Book":
    st.markdown('<div class="section-header">📤 Return a Book</div>', unsafe_allow_html=True)
    book_id = st.number_input("Enter Book ID to return:", min_value=1, step=1)
    if st.button("Return"):
        msg = library.return_book(user, book_id)
        if "returned" in msg:
            st.success(msg)
        else:
            st.warning(msg)

elif menu == "View My Borrowed Books":
    st.markdown(f'<div class="section-header">🎒 {user.name}\'s Borrowed Books</div>', unsafe_allow_html=True)
    if user.borrowed_books:
        for book in user.borrowed_books:
            render_book_card(book)
    else:
        render_empty("No borrowed books")

elif menu == "Add New Book":
    st.markdown('<div class="section-header">➕ Add a New Book</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Book Title")
        book_id = st.number_input("Book ID", min_value=1, step=1)
    with col2:
        author = st.text_input("Author")
        total_copies = st.number_input("Total Copies", min_value=1, step=1)
    if st.button("Add Book"):
            new_book = Book(title, author, book_id, total_copies)
            library.add_books(new_book)
            st.success(f"Book '{title}' added successfully!")
