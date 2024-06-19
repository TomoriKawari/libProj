from sqlalchemy import (Integer, ForeignKey, Column, String,
                        DateTime, Boolean)
from sqlalchemy.orm import relationship, backref
from myapp import BaseModel, Base


class Book(BaseModel):
    __tablename__ = 'book'
    author_id = Column(String(length=36), ForeignKey('author.id'), index=True)
    publisher_id = Column(String(length=36), ForeignKey('publisher.id'), index=True)
    publication_date = Column(DateTime, index=True)
    title = Column(String(length=255), nullable=False, index=True)

    authors = relationship('Author')
    publishers = relationship('Publisher')

    branches = relationship('LibraryBranch',
                            secondary='book_branch',
                            back_populates='books',
                            foreign_keys='[book_branch.c.book_id, book_branch.c.branch_id]')


