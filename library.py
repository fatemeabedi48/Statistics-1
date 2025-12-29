class Book:  
    def __init__(self, name):  
        self.name = name  
        self.next = None  

class Library:  
    def __init__(self):  
        self.first = None  
        self.last = None  

    def add_left(self, book_name):  
        if book_name:  
            new_book = Book(book_name)  
            new_book.next = self.first  
            self.first = new_book  
            if self.last is None:  
                self.last = new_book  

    def add_right(self, book_name):  
        if book_name:  
            new_book = Book(book_name)  
            if self.last:   
                self.last.next = new_book  
            self.last = new_book  
            if self.first is None:   
                self.first = new_book  

    def remove_left(self):  
        if self.first is not None:   
            temp = self.first  
            self.first = self.first.next  
            del temp    
            if self.first is None:  
                self.last = None  

    def print_books(self):  
        current = self.first  
        count = 0  
        
        while current:  
            count += 1  
            current = current.next  

        print(count)  
        current = self.first  

        while current:  
            print(current.name)  
            current = current.next  

if __name__ == "__main__":  
    library = Library()  
    n = int(input())  

    for _ in range(n):  
        book_name = input().rstrip()  
        library.add_right(book_name)  

    while True:  
        command = input().strip()  
        if command == "Exit":  
            break  
        elif command == "AddLeft":  
            book_name = input().strip()  
            library.add_left(book_name)  
        elif command == "AddRight":  
            book_name = input().strip()  
            library.add_right(book_name)  
        elif command == "DeleteLeft":  
            library.remove_left()  

    library.print_books()
