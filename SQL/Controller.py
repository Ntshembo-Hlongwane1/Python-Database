import sqlite3


def create_new_book() -> None:

  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()

  cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
  connection.commit()

  connection.close()



def add_new_book(name, author) -> None:

  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()

  cursor.execute('INSERT INTO books VALUES(?, ?, ?)', (name, author, 0))
  connection.commit()

  connection.close()


def get_all_books() -> list:

  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()

  cursor.execute('SELECT books.name, books.author, books.read FROM books')

  books = [{'name':row[0], 'author':row[1], 'read':row[2]} for row in cursor.fetchall()]

  return books 

def mark_book_as_read(name, author) -> str:

  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()

  cursor.execute('UPDATE books SET read=1 WHERE name=? and author=?', (name, author))
  connection.commit()
  connection.close()

  return '\nUpdated'


def delete_book(name, author):

  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()

  cursor.execute('DELETE FROM books WHERE name=? and author=?', (name, author))
  connection.commit()

  connection.close()
  return '\d DELETED'


def search_book(name, author) -> list:

  connection = sqlite3.connect('data.db')
  cursor = connection.cursor()

  cursor.execute('SELECT books.name, books.author, books.read FROM books WHERE books.name=? and books.author=?', (name, author))

  book = [{'name':row[0], 'author':row[1], 'read':row[2]} for row in cursor.fetchall()]

  return book

