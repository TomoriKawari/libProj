from sqlalchemy import select
from sqlalchemy.orm import joinedload

from myapp import db_session
from src.models import Book, Author


# Tìm tất cả các cuốn sách của một tác giả cụ thể, sắp xếp theo ngày xuất bản.
def get_book_same_author_sort_date(author_name: str):
    with db_session() as session:
        books_by_author = session.query(Book).join(Author).filter(Author.name == author_name).order_by(
            Book.publication_date).all()
    for book in books_by_author:
        print(f'Title: {book.title}, Publication Date: {book.publication_date}')


get_book_same_author_sort_date('Author 1')
