from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repositories


def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (?,?,?) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book


def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repositories.select(row["author_id"])
        book = Book(row["title"], row["genre"], author, row["id"])
        books.append(book)
    return books


def delete(id):
    sql = "DELETE FROM books WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
