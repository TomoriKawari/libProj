from sqlalchemy import select
from sqlalchemy.orm import joinedload

from myapp import db_session
from src.models import Book, LibraryBranch, book_branch
from sqlalchemy import func


# Tính tổng số sách tại mỗi chi nhánh thư viện.
def get_total_books_per_branch():
    with db_session() as session:
        total_books_per_branch = session.query(LibraryBranch.name,
                                               func.sum(book_branch.columns.quantity))

        total_books_per_branch = total_books_per_branch.join(book_branch,
                                                             LibraryBranch.id == book_branch.columns.branch_id)

        total_books_per_branch = total_books_per_branch.group_by(LibraryBranch.name).all()

    for branch_name, total_books in total_books_per_branch:
        print(f'Branch: {branch_name}, Total Books: {total_books}')


get_total_books_per_branch()
