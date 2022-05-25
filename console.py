import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()


author_1 = Author("J.K", "Rowling")
author_repository.save(author_1)

author_2 = Author("Stephen", "King")
author_repository.save(author_2)

book_1 = Book("The Philosopher's Stone", "Fantasy", author_1)
book_repository.save(book_1)

book_2 = Book("The Chamber of Secrets", "Fantasy", author_1)
book_repository.save(book_2)

book_3 = Book("The Prisoner of Azkaban", "Fantasy", author_1)
book_repository.save(book_3)

book_4 = Book("Misery", "Horror", author_2)
book_repository.save(book_4)
