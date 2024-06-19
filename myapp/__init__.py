import datetime
import uuid

from sqlalchemy import Integer, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __tablename__ = 'BaseModel'
    __table_args__ = {'extend_existing': True}
    __abstract__ = True  # Doesn't need table
    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    # create_time = Column(DateTime, default=datetime.datetime.now, index=True)
    # update_time = Column(DateTime, default=datetime.datetime.now, index=True)
    pass


engine = create_engine("mysql://root:taolavu18112005@localhost/libprojthird")
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
