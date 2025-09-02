"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(**book):
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """
    
    if "id" not in book or "title" not in book or "author" not in book:
        return "Book must have id, title, and author!"
    else:
        for item in library:
            if item["id"] == book["id"]:
                return f"Book with ID {book['id']} Already exist"
            
        book.setdefault("available", True)
        library.append(book)
    
        return f"Book '{book['title']}' has been added successfully!!"
    

def search_books(*search_param):
    """Search for books by multiple keywords (title, author).
    return books that match search description.
    """
    outcome = []
   
    for book in library:
       for keyword in search_param:
           if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
               outcome.append(book)
               break
    return f"Results of search: {outcome}"
       

def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """
    for item in library:
        
        if book_id == item["id"]:
            if item["available"]:
                item["available"] = False
                return f"You have borrowed '{item['title']}'..."
            else:
                return f"'{item['title']}' is not Available"
        else:
            return f"Book not found!!"