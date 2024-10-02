import datetime
from datetime import timedelta

class Book:
    def __init__(self, title, author,cover_artist, description, pub_date, isbn, copies_available):
          self.title = title
          self.author = author
          self.cover_artist = cover_artist
          self.description = description
          self.pub_date = pub_date
          self.isbn = isbn
          self.copies_available = copies_available
          self.checked_out_by = []
          self.history_log = [] 

    def checkout(self, name):
        if self.copies_available > 0:
            self.checked_out_by.append(name)
            self.copies_available -= 1
            self.history_log.append((name, "borrowed", datetime.datetime.now()))
            print(f"{name} checked out '{self.title}'")
        else:
            print(f"All copies of '{self.title}' are currently checked out.")
         

    def check_in(self, name):
        if name in self.checked_out_by:
            self.checked_out_by.remove(name)
            self.copies_available += 1
            self.history_log.append((name, "returned", datetime.datetime.now()))
            print(f"{name} returned '{self.title}'")
        else:
            print(f"{name} did not check out this book.")

    def print_history(self):
        print("------------------------------------------------")
        print(f"History of '{self.title}':")
        print("------------------------------------------------")
        for record in self.history_log:
            name, action, date = record
            print(f"{name} {action} the book on {date.strftime('%Y-%m-%d %H:%M:%S')}")

        

    def add_copies(self, number):
         self.copies_available += number

    def remove_copies(self, number):
        if number <= self.copies_available:
            self.copies_available -= number
        else:
            print("Not enough copies to remove.")

class LibraryCard:
    def __init__(self, member_name):
        self.member_name = member_name
        self.borrowing_history = {}  

    def borrow_book(self, book_title, due_date):
        self.borrowing_history[book_title] = due_date

    def return_book(self, book_title):
        if book_title in self.borrowing_history:
            del self.borrowing_history[book_title]

    def calculate_fines(self):
        today = datetime.datetime.now()
        total_fines = 0
        for book_title, due_date in self.borrowing_history.items():
            if today > due_date:
                overdue_days = (today - due_date).days
                fine = overdue_days * 1  
                total_fines += fine
                print(f"Fine for '{book_title}': Rs. {fine}")
        return total_fines  



class Member:
    def __init__(self, name):
        self.name = name
        self.library_card = LibraryCard(name) 

    def borrow_book(self, library, book_title, due_date):
        if library.lend_book(book_title, self.name):
             self.library_card.borrow_book(book_title, due_date)

    def return_book(self, library, book_title):
        library.return_book(book_title, self.name)
        self.library_card.return_book(book_title)

        overdue_fines = self.library_card.calculate_fines()
        if overdue_fines > 0:
            print(f"Total overdue fines for {self.name}: Rs. {overdue_fines}")
        else:
            print(f"No fines for {self.name}.")

class Librarian:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def add_new_book(self, book):
        self.library.add_book(book)

    def manage_book_lending(self, member, book_title, due_date):
        member.borrow_book(self.library, book_title, due_date)



class Library:
    def __init__(self, list_of_books):
        self.availablebooks = list_of_books

    def display_available_books(self):
        print("==========================================")
        print("The books availabel in the library are:")
        print("==========================================")
        for book in self.availablebooks:
            print(f"Title : {book.title} \nCopies available : {book.copies_available}")
      
    def lend_book(self,requested_book_title, member_name):
        for book in self.availablebooks:
            if book.title == requested_book_title:
                book.checkout(member_name)
                return True
        print(f"'{requested_book_title}' is not available in the library.")
        return False
                
        

    def return_book(self, returned_book_title, member_name):
        for book in self.availablebooks:
            if book.title == returned_book_title:
                book.check_in(member_name)
                return
        print(f"'{returned_book_title}' does not belong to our library.")


    def search_book(self, search_term):
        print(f"Searching for books with '{search_term}'...")
        results = []
        for book in self.availablebooks:
            if (search_term.lower() in book.title.lower() or
                search_term.lower() in book.author.lower() or
                search_term.lower() in book.isbn.replace('-', '').lower()):
                results.append(book)
        
        if results:
            print("Search Results:")
            for book in results:
                print(f"Title: {book.title} | Author: {book.author} | Copies: {book.copies_available}")
        else:
            print(f"No books found matching '{search_term}'.")


    def add_book(self,new_book):
            self.availablebooks.append(new_book)
            print(f"'{new_book.title}' added to the library")


    def remove_book(self, book_title):
        for book in self.availablebooks:
            if book.title == book_title:
                self.availablebooks.remove(book)
                print(f"'{book.title}' has been removed from the library.")
                return
        print(f"Book '{book_title}' not found in the library's inventory.")



book1 = Book(title = "Wings of fire",
             author = "	A P J Abdul Kalam",
             cover_artist = "Photograph courtesy: The Week",
             description = "About the life of A.P.J.Abdul Kalam",
             isbn = "81-7371-146-1 (paperback edition)",
             pub_date = "1999",
             copies_available = 10
             )

book2 = Book(
    title="Fast Track Objective Arithmetic",
    author="Rajesh Verma",
    cover_artist="Illustration by XYZ",
    description="About the metal ability",
    isbn="9312149830",
    pub_date="2018",
    copies_available = 10,
    
)


book3 = Book(title="To Kill a Mockingbird", 
             author="Harper Lee", 
             cover_artist="Illustration by ABC", 
             description="A novel about racism and injustice.", 
             isbn="978-0060935467", 
             pub_date="1960", 
             copies_available=5)


books_list = [book1, book2, book3]
library = Library(books_list)
library.display_available_books()

# Create a member
member1 = Member(name="Mala")
member2 = Member(name="Vanitha")

print("\n--Checking out 'Wings of fire'--")
member1.borrow_book(library, "Wings of fire", datetime.datetime.now() + timedelta(days=14))
member2.borrow_book(library, "Wings of fire", datetime.datetime.now() + timedelta(days=14))
library.display_available_books()

print("\n--Borrowing History before returning--")
print(member1.library_card.borrowing_history)

print("\n--Returning 'Wings of fire'--")
member1.return_book(library, "Wings of fire")
library.display_available_books()

# Checking the borrowing history after returning the book
print("\n--Borrowing History after returning--")
print(member1.library_card.borrowing_history)  # Should show an empty dictionary

# Searching for a book 
print("\n-----Searching for a book by title, author, isbn-----")
library.search_book("Wings of fire")

library.search_book("Harper Lee")

library.search_book("9312149830")

new_book = Book(title="XXXXX",
    author="YYYYY",
    cover_artist="Illustration by XYZ",
    description="A novel",
    isbn="1234567890",
    pub_date="1949",
    copies_available=8)

print("\n--Adding new book to the library--")
library.add_book(new_book)
library.display_available_books()
print("\n--Removing a book from the library--")
library.remove_book("XXXXX")
library.display_available_books()

# Calculate fines (if any)
print("\n--Calculating fines--")
total_fines = member2.library_card.calculate_fines()
print(f"Total fines: Rs. {total_fines}")

book1.print_history()
