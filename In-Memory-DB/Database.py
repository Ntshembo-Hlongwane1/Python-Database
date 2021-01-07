books = []

def add_new_book(name, author) -> None:
  books.append({'book_name': name, 'book_author':author, 'read':False})



def list_books() -> list:
  return books


def mark_book_as_read(name, author) -> str:

  for book in books:
    if (book['book_name'] == name and book['book_author'] == author):
      book['read'] = True

  return 'DONE'

def delete_book(name, author) -> list:

  global books
  books = [book for book in books if book['book_name'] != name and book['book_author'] != author]

  return books


def find_specific_book(name, author) -> object:

  for book in books:
    if (book['book_name'] == name and book['book_author'] == author):
      return book
  
  return {}

