from sqlalchemy import select
from sqlalchemy.orm import Session


from src.models import Author, Book, LibraryBranch, book_branch
from myapp import db_session


# Lấy danh sách các tác giả có sách được lưu trữ ở một chi nhánh cụ thể.
def get_author_same_branch(library_branch_name: str) -> Author:
    with db_session() as session:
        branch = session.query(LibraryBranch).filter_by(name=library_branch_name).all()

        for branch in branch:
            authors = session.query(Author).join(Book).join(book_branch).filter(
                book_branch.c.branch_id == branch.id).all()
        for author in authors:
            return author.name


print(get_author_same_branch('Branch 1'))
