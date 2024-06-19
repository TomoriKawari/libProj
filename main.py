import asyncio
from datetime import datetime

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List

from myapp import db_session
from src.models import Author as AuthorModel, Publisher as PublisherModel
from src.models import LibraryBranch as LibraryBranchModel, Book as BookModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



# Define Pydantic Author models
class Author(BaseModel):
    name: str | None = None
    birthdate: datetime | None = None
    id: str
    class Config:
        from_attributes = True


# Define Pydantic Publisher models
class Publisher(BaseModel):
    name: str | None = None
    address: str | None = None
    id: str
    class Config:
        from_attributes = True


# Define Pydantic Library Branch models
class LibraryBranch(BaseModel):
    name: str | None = None
    address: str | None = None
    id: str
    class Config:
        from_attributes = True


# Define Pydantic Book models
class Book(BaseModel):
    title: str | None = None
    publication_date: datetime | None = None
    id: str
    class Config:
        from_attributes = True





# Get all current authors
@app.get("/author/", response_model=List[Author])
async def get_all_authors():
    with db_session() as session:
        authors = session.query(AuthorModel).all()
    return authors

# Get author based on ID
@app.get("/author/{author_id}", response_model=Author)
async def get_author_by_id(author_id: str):
    with db_session() as session:
        author = session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
    return author

# Create new author
@app.post("/author/", response_model=Author)
async def create_author(author: Author):
    with db_session() as session:
        author = AuthorModel(**author.dict())
        session.add(author)
        session.commit()
        session.refresh(author)
    return author

# Update author based on ID
@app.put("/author/{author_id}", response_model=Author)
async def update_author(author_id: str, author_update: Author):
    with db_session() as session:
        author = session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        author.name = author_update.name
        author.birthdate = author_update.birthdate
        session.commit()
        session.refresh(author)
    return author

# Delete author based on ID
@app.delete("/author/{author_id}", response_model=Author)
async def delete_author(author_id: str):
    with db_session() as session:
        author = session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        session.delete(author)
        session.commit()
        session.refresh(author)
    return author





# Get all current publishers
@app.get("/publisher/", response_model=List[Publisher])
async def get_all_publishers():
    with db_session() as session:
        publishers = session.query(PublisherModel).all()
    return publishers

# Get publisher based on ID
@app.get("/publisher/{publisher_id}", response_model=Publisher)
async def get_publisher_by_id(publisher_id: str):
    with db_session() as session:
        publisher = session.query(PublisherModel).filter(PublisherModel.id == publisher_id).first()
        if publisher is None:
            raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

# Create new publisher
@app.post("/publisher/", response_model=Publisher)
async def create_publisher(publisher: Publisher):
    with db_session() as session:
        publisher = PublisherModel(**publisher.dict())
        session.add(publisher)
        session.commit()
        session.refresh(publisher)
    return publisher

# Update publisher based on ID
@app.put("/publisher/{publisher_id}", response_model=Publisher)
async def update_publisher(publisher_id: str, publisher_update: Publisher):
    with db_session() as session:
        publisher = session.query(PublisherModel).filter(PublisherModel.id == publisher_id).first()
        if publisher is None:
            raise HTTPException(status_code=404, detail="Publisher not found")
        publisher.name = publisher_update.name
        publisher.address = publisher_update.address
        session.commit()
        session.refresh(publisher)
    return publisher

# Delete publisher based on ID
@app.delete("/publisher/{publisher_id}", response_model=Publisher)
async def delete_publisher(publisher_id: str):
    with db_session() as session:
        publisher = session.query(PublisherModel).filter(PublisherModel.id == publisher_id).first()
        if publisher is None:
            raise HTTPException(status_code=404, detail="Publisher not found")
        session.delete(publisher)
        session.commit()
        session.refresh(publisher)
    return publisher





# Get all current library branches
@app.get("/library/", response_model=List[LibraryBranch])
async def get_all_libraries():
    with db_session() as session:
        libraries = session.query(LibraryBranchModel).all()
    return libraries

# Get library branch based on ID
@app.get("/library/{library_id}", response_model=LibraryBranch)
async def get_library_by_id(library_id: str):
    with db_session() as session:
        library = session.query(LibraryBranchModel).filter(LibraryBranch.id == library_id).first()
        if library is None:
            raise HTTPException(status_code=404, detail="Library not found")
    return library

# Create new library branch
@app.post("/library/", response_model=LibraryBranch)
async def create_library(library: LibraryBranch):
    with db_session() as session:
        library = LibraryBranchModel(**library.dict())
        session.add(library)
        session.commit()
        session.refresh(library)
    return library

# Update library branch based on ID
@app.put("/library/{library_id}", response_model=LibraryBranch)
async def update_library(library_id: str, library_update: LibraryBranch):
    with db_session() as session:
        library = session.query(LibraryBranchModel).filter(LibraryBranchModel.id == library_id).first()
        if library is None:
            raise HTTPException(status_code=404, detail="Library not found")
        library.name = library_update.name
        library.address = library_update.address
        session.commit()
        session.refresh(library)
    return library

# Delete library branch based on ID
@app.delete("/library/{library_id}", response_model=LibraryBranch)
async def delete_library(library_id: str):
    with db_session() as session:
        library = session.query(LibraryBranchModel).filter(LibraryBranchModel.id == library_id).first()
        if library is None:
            raise HTTPException(status_code=404, detail="Library not found")
        session.delete(library)
        session.commit()
        session.refresh(library)
    return library





# Get all current books
@app.get("/book/", response_model=List[Book])
async def get_all_books():
    with db_session() as session:
        books = session.query(BookModel).all()
    return books

# Get book based on ID
@app.get("/book/{book_id}", response_model=Book)
async def get_book_by_id(book_id: str):
    with db_session() as session:
        book = session.query(BookModel).filter(BookModel.id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
    return book

# Create new book
@app.post("/book/", response_model=Book)
async def create_book(book: Book):
    with db_session() as session:
        book = BookModel(**book.dict())
        session.add(book)
        session.commit()
        session.refresh(book)
    return book

# Update book based on ID
@app.put("/book/{book_id}", response_model=Book)
async def update_book(book_id: str, book_update: Book):
    with db_session() as session:
        book = session.query(BookModel).filter(BookModel.id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        book.title = book_update.title
        book.publication_date = book_update.publication_date
        session.commit()
        session.refresh(book)
    return book

# Delete book based on ID
@app.delete("/book/{book_id}", response_model=Book)
async def delete_book(book_id: str):
    with db_session() as session:
        book = session.query(BookModel).filter(BookModel.id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        session.delete(book)
        session.commit()
        session.refresh(book)
    return book
