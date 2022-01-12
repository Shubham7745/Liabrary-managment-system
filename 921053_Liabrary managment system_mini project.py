class Library:
    def __init__(self,list,name):
        self.booksList=list
        self.name=name
        self.lendDict={ }
    def displayBooks(self):
        print(f"we have following books in our Library: {self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated.you can take book now")
        else:
            print(f"Book is already being used by{self.lendDict[book]}")

    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list")
    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    shubham=Library(['python','Rich Daddy poor Daddy','Harry potter','C++Basics','Algorithms by CLRS'], "codewithshubham")
    while(True):
          print(f"welcome to the {shubham.name} library.Enter your choice to continue")
          print("1.Display Books")
          print("2.lend a Book")
          print("3.Add a Book")
          print("4.Return a Book")
          user_choice=int(input())

          if user_choice==1:
              shubham.displayBooks()
          elif user_choice==2:
              book=input("Enter the name of book want to lend:")
              user=input("Enter your name")
              shubham.lendBook(user,book)

          elif user_choice==3:
              book=input("Enter the name of book want to add:")
              shubham.addBook(book)
          elif user_choice==4:
              book=input("Enter the name of book want to return:")
              shubham.returnBook(book)

          else:

              print("Not a valid option")
          print("press q to quit and c to continue")
          user_choice2=" "
          while(user_choice2!="c" and user_choice2!="q"):
              user_choice2=input()
              if user_choice2=="q":
                  exit()








