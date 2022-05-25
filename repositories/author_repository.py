from db.run_sql import run_sql

from models.author import Author
from models.book import Book


def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (?,?) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    author.id = id
    return author


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result["first_name"], result["last_name"], result["id"])
    return author


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
