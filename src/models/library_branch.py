from sqlalchemy import (Integer, ForeignKey, Column, String,
                        DateTime, Boolean)
from sqlalchemy.orm import relationship, backref
from myapp import BaseModel


class LibraryBranch(BaseModel):
    __tablename__ = 'library_branch'
    name = Column(String(length=255), nullable=False, index=True)
    address = Column(String(length=255), index=True)

    books = relationship('Book',
                         secondary='book_branch',
                         back_populates='branches',
                         foreign_keys='[book_branch.c.book_id, book_branch.c.branch_id]')


