from sqlalchemy import (Integer, ForeignKey, Column, String,
                        DateTime, Boolean)
from sqlalchemy.orm import relationship, backref
from myapp import BaseModel


class Author(BaseModel):
    __tablename__ = 'author'
    name = Column(String(length=255), nullable=False, index=True)
    birthdate = Column(DateTime, index=True)