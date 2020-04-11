from utils import database

USER_CHOICE = """
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark book as read
-'d' to delete a book
-'q' to quit
"""

def menu():
  database.check_exist()
  while True:
    user_input = input(USER_CHOICE)
    if user_input == "q":
      break
    elif user_input == "a":
      prompt_add_book()
    elif user_input == "l":
      list_books()
    elif user_input == "r":
      prompt_read_book()
    elif user_input == "d":
      prompt_delete_book()
    else:
      print("Invalid input, please try again")


def prompt_add_book():
  name = input("Enter the name of the book:")
  author = input("Enter the author of the book:")
  database.add_book(name,author)


def list_books():
  books = database.return_books()
  for book in books:
    read = "Yes" if book['read'] == "1" else "No"
    print(f"Name:{book['name']}\nAuthor:{book['author']}\nread:{read}\n")
    #Name:Something
    #Author:Someone
    #Read:True/False


def prompt_read_book():
  book_name = input("Enter the name of the book:")
  database.read_book(book_name)


def prompt_delete_book():
  book_name = input("Enter the book you want to delete:")
  database.delete_book(book_name)


if __name__ == "__main__":
  menu()