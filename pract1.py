class book :
    def __init__(self , title, author):
        self.title = title
        self.author = author
        self.available = True
        
        
        def display(self):
            status = "available" if self.avilable else "Borrowed"
            print(f"title: {self.title}, author: {self.author}, status: {status}")
            
            class patron:
                def __init__(self, name):
                    self.name = name
                    self.borrowed_books = []
                    
                    
                    def display(self):
                        print(f"patron : {self.name}")
                        if self.borrowed_books:
                            print("borrowed books:")
                            for book in self.borrowed_books:
                                print("-", book.title)
                                
                                
                            else:
                                print(" no books borrowed.")
                                
                                
                                class library:
                                    def __init__(self):
                                        self.book = []
                                        self.patrons = []
                                        
                                        
                                        def add_book(self, title, author):
                                            book = book(title , author)
                                            self.books.append(book)
                                            print(f"book '{title}' added successfully.")
                                            
                                            
                                            def register_patron(self, name):
                                                patron = patron(name)
                                                self.patrons.append(patron)
                                                print(f"patron '{name}' registered successfully.")
                                                
                                                
                                                def borrow_book(self, patron_name , book_title):
                                                    patron = next((p for p in self.patrons if p.name == patron_name), None)
                                                    book = next((b for b in self.books if b.title == book_title), None)

                                                    if patron and book:
                                                        if book.available:
                                                            book.available = False
                                                            patron.borrowed_books.append(book)
                                                            print(f"{patron_name} borrowed '{book_title}'.")
                                                        else:
                                                            print("book is already borrowed.")
                                                    else:
                                                            print("patron or book not found.")
                                                            
                                                            def return_book(self, patron_name, book_title):
                                                                patron = next((p for p in self.patrons if p.name == patron_name), None)
                                                                
                                                                
                                                                if patron:
                                                                    for book in patron.borrowed_books:
                                                                        if book.title == book_title:
                                                                            book.available = True
                                                                            patron.borrowed_books.remove(book)
                                                                            print(f"{patron_name} returned '{book_title}'.")
                                                                            return
                                                                    print("book not borrowed by this patron.")
                                                                else:
                                                                    print("patron not found.")
                                                                    
                                                                    def show_books(self):
                                                                        if self.books:
                                                                            print("\nLibrary books:")
                                                                            for book in self.books:
                                                                                book.display()
                                                                          
                                                                          
                                                                            def show_patrons(self):
                                                                                if self.patrons:
                                                                                    print("\nRegistered patrons:")
                                                                                    for patron in self.patrons:
                                                                                        patron.display()
                                                                                        
                                                                                        
                                                                                        library = library()
                                                                                        
                                                                                        library.add_book("Python basics", "John smith")
                                                                                        library.add_book("Data structures", "alice brown")
                                                                                        
                                                                                        library.register_patron("Rahul")
                                                                                        library.register_patron("Priya")
                                                                                        
                                                                                        
                                                                                        library.borrow_book("Rahul", "Python basics")
                                                                                        
                                                                                        
                                                                                        library.show_books()
                                                                                        library.show_patrons()
                                                                                        
                                                                                        library.return_book("Rahul", "Python basics")
                                                                                        
                                                                                        library.show_books()
                                                                                        
                                                                                        