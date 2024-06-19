from sqlalchemy import select
from sqlalchemy.orm import joinedload

from myapp import db_session
from src.models import Book, LibraryBranch


# Lấy danh sách tất cả các sách cùng với tên tác giả và tên nhà xuất bản.
def get_book_same_author_publisher():
    with db_session() as session:
        stmt = session.query(Book).order_by(Book.author_id).order_by(Book.publisher_id).all()
        for row in stmt:
            print(f'{row.title} {row.publication_date}')


get_book_same_author_publisher()
