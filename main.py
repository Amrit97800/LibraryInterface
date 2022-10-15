class Library:
    def __init__(self,lisOfBooks):
        self.books=lisOfBooks

    def displayAvailableBooks(self):
        print("Books available in the library are:")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it in 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("This book is either not avilable or has been issued to someone else. Please wait until the book is available." )
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!\n\tHope you enjoy it reading\n\tHave a great day ahead!")



class Student:
    
    def requestBook(self):
        self.Book=input("Enter the name of Book you want to borrow: ")
        return self.Book

    def returnBook(self):
        self.Book=input("Enter the name of Book you want to return/add: ")
        return self.Book

if __name__=="__main__":
    centraLibrary= Library(["Algorithms","Django","Clrs","Python Notes"])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    
    while(True):
        welcomeMsg='''
        ====Welcome to central library====
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the Library'''

        print(welcomeMsg)


        a=int(input("Enter a choice : "))
        if a==1:
            centraLibrary.displayAvailableBooks()
        elif a==2:
            centraLibrary.borrowBook(student.requestBook())
        elif a==3:
            centraLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central library.\nHave a great day ahead.")
            break
        else:
            print("Invalid choice")
