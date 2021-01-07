import Database


choices = """

  Choice one of the options to proceed:

  a - To add new book
  l - To list all books
  s - To search for a book
  r - Mark a book as read 
  d - To delete a book 
  q - To quit
  \n
"""

def Main():

  user_input = input(choices)

  while user_input != 'q':

    if (user_input.lower() == 'a'):
      prompt_add_new_book()

    elif user_input.lower() == 'l':
      list_books()

    elif user_input.lower() == 's':
      prompt_search_book()

    elif user_input.lower() == 'r':
      prompt_mark_book_as_read()

    elif user_input.lower() == 'd':
      prompt_delete_book()

    else:
      print(F'UNKNOWN command: {user_input}, please try again. ')

    user_input = input(choices)


def list_books() -> None :
  books = Database.list_books()
  count = 1
  for book in books:
    read = "YES" if book['read'] else 'NO'
    print(f"\n#{count} Book name: {book['book_name']}, Book author: {book['book_author']}, isBookRead: {read}")
    count += 1



def prompt_add_new_book() -> None:

  name = input('Enter name of the book: ')
  author = input(f"Enter name of the Author of '{name}': ")

  books = Database.add_new_book(name, author)
 


def prompt_search_book() -> None:

  name = input('\nEnter the name of the book you want to search: ')
  author = input(f'Enter the name of the author that wrote {name} book: ')
  
  book = Database.find_specific_book(name, author)
  if (book == {}):
    print(f"\nNo book with the name: '{name}' written by '{author}' exists: ")
  else:
    read = "YES" if book['read'] else 'NO'
    print(f"\n Results --> Book name: {book['book_name']}, Book author: {book['book_author']}, isBookRead: {read}")

def prompt_mark_book_as_read() -> None:

  name = input('\nEnter the name of the book that you want to mark as read: ')
  author = input(f"Who is the Author of the book, that you read called: {name}. ")

  results = Database.mark_book_as_read(name, author)

  print(results)

def prompt_delete_book() -> None:
  
  confirm_deletion = input('Are you sure you want to proceed with deleting? Y/N: ').lower()

  if (confirm_deletion == 'y'):
    name= input('\nWhat is the name of the book that you want delete: ')
    author = input(f"Who is the of the book '{name}' that you want to delete: ")
    Database.delete_book(name, author)
    list_books()

  else:
    print('Aborting deletion of book request..')




if __name__ == "__main__":
    Main()