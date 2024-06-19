import datetime
from sqlalchemy import insert
from sqlalchemy.orm import Session

from myapp import db_session
from src.models import Book, book_branch, LibraryBranch, Author, Publisher

# Check if book already exists in table (same title + publication date)
with db_session() as session:
    # Insert library branches
    branch_1 = LibraryBranch(
        name='Branch 1',
        address='Address 1'
    )
    branch_2 = LibraryBranch(
        name='Branch 2',
        address='Address 2'
    )
    branch_3 = LibraryBranch(
        name='Branch 3',
        address='Address 3'
    )

    # Insert authors
    author_1 = Author(
        name='Author 1',
        birthdate=datetime.datetime(1998, 1, 1)
    )
    author_2 = Author(
        name='Author 2',
        birthdate=datetime.datetime(1998, 1, 2)
    )
    author_3 = Author(
        name='Author 3',
        birthdate=datetime.datetime(1998, 1, 3)
    )

    # Insert publishers
    publisher_1 = Publisher(
        name='Publisher 1',
        address='Address 1',
    )
    publisher_2 = Publisher(
        name='Publisher 2',
        address='Address 2',
    )
    publisher_3 = Publisher(
        name='Publisher 3',
        address='Address 3',
    )

    # Insert books
    book_1 = Book(
        title='Book 1',
        publication_date=datetime.datetime(1998, 1, 13),
        author_id=author_1.id,
        publisher_id=publisher_1.id
    )
    book_2 = Book(
        title='Book 2',
        publication_date=datetime.datetime(1998, 1, 14),
        author_id=author_2.id,
        publisher_id=publisher_2.id
    )
    book_3 = Book(
        title='Book 3',
        publication_date=datetime.datetime(1998, 1, 15),
        author_id=author_3.id,
        publisher_id=publisher_3.id
    )

    session.add_all([book_1, book_2, book_3,
                    branch_1, branch_2, branch_3,
                    author_1, author_2, author_3,
                    publisher_1, publisher_2, publisher_3])
    session.commit()

    # Insert book branches
    session.execute(book_branch.insert().values(book_id=book_1.id, branch_id=branch_1.id, quantity=4))
    session.execute(book_branch.insert().values(book_id=book_2.id, branch_id=branch_2.id, quantity=13))
    session.execute(book_branch.insert().values(book_id=book_3.id, branch_id=branch_3.id, quantity=7))
    session.commit()
