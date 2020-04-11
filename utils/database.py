book_file = 'books.txt'

def check_exist():
  try:
    open("books.txt","a")
  except Error:
    pass
  

def add_book(name,author):
  with open(book_file,"a") as file: #opens books 
    file.write(f"{name},{author},0\n") #writes to book


def return_books():
  with open(book_file,"r") as file:
    lines = [line.strip().split(",") for line in file.readlines()] #strips/splits the lines so they look like this:
    #[[name,author,read],[name,author,read]]

  return [
    {'name':line[0], 'author':line[1],'read':line[2]}
    for line in lines
  ]


def read_book(book_name):
  books = return_books()
  for book in books:
    if book['name'] == name:
      book['read'] = 1
  
  _save_all_books(books) #underscore means you should not call the function


def _save_all_books(books):
  with open(book_file,"w") as file:
    for book in books:
      file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(book_name):
  books = return_books()
  books = [book for book in books if book['name'] != book_name]
  _save_all_books(books)
