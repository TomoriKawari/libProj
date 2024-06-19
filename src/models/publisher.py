from sqlalchemy import (Integer, ForeignKey, Column, String,
                        DateTime, Boolean)
from sqlalchemy.orm import relationship, backref
from myapp import BaseModel


class Publisher(BaseModel):
    __tablename__ = 'publisher'
    name = Column(String(length=255), nullable=False, index=True)
    address = Column(String(length=255), index=True)
