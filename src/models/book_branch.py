from sqlalchemy import (Integer, ForeignKey, Column, String,
                        DateTime, Boolean, Table)
from sqlalchemy.orm import relationship, backref
from myapp import BaseModel

book_branch = Table("book_branch",
                    BaseModel.metadata,
                    Column('book_id', ForeignKey('book.id'), index=True),
                    Column("branch_id", ForeignKey('library_branch.id'), index=True),
                    Column("quantity", Integer, index=True))
