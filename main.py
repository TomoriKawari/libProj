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
class AuthorSchema(BaseModel):
    name: str | None = None
    birthdate: datetime | None = None

    class Config:
        from_attributes = True


# Define Pydantic Publisher models
class PublisherSchema(BaseModel):
    name: str | None = None
    address: str | None = None

    class Config:
        from_attributes = True


# Define Pydantic Library Branch models
class LibraryBranchSchema(BaseModel):
    name: str | None = None
    address: str | None = None

    class Config:
        from_attributes = True


# Define Pydantic Book models
class BookSchema(BaseModel):
    title: str | None = None
    publication_date: datetime | None = None

    class Config:
        from_attributes = True


# Get all current authors
@app.get("/author/", response_model=List[AuthorSchema])
async def get_all_authors():
    with db_session() as session:
        authors = session.query(AuthorModel).all()
    return authors


# Get author based on ID
@app.get("/author/{author_id}", response_model=AuthorSchema)
async def get_author_by_id(author_id: str):
    with db_session() as session:
        author_found = session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if author_found is None:
            raise HTTPException(status_code=404, detail="Author not found")
    return author_found


# Create new author
@app.post("/author/", response_model=AuthorSchema)
async def create_author(author_create: AuthorSchema):
    with db_session() as session:
        author_found = AuthorModel(**author_create.dict())
        session.add(author_found)
        session.commit()
        session.refresh(author_found)
    return author_create


# Update author based on ID
@app.put("/author/{author_id}", response_model=AuthorSchema)
async def update_author(author_id: str, author_update: AuthorSchema):
    with db_session() as session:
        author_found = session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if author_found is None:
            raise HTTPException(status_code=404, detail="Author not found")
        author_found.name = author_update.name
        author_found.birthdate = author_update.birthdate
        session.commit()
        session.refresh(author_found)
    return author_found


# Delete author based on ID
@app.delete("/author/{author_id}", response_model=AuthorSchema)
async def delete_author(author_id: str):
    with db_session() as session:
        author_found = session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if author_found is None:
            raise HTTPException(status_code=404, detail="Author not found")
        session.delete(author_found)
        session.commit()
        session.refresh(author_found)
    return author_found


# Get all current publishers
@app.get("/publisher/", response_model=List[PublisherSchema])
async def get_all_publishers():
    with db_session() as session:
        publishers = session.query(PublisherModel).all()
    return publishers


# Get publisher based on ID
@app.get("/publisher/{publisher_id}", response_model=PublisherSchema)
async def get_publisher_by_id(publisher_id: str):
    with db_session() as session:
        publisher_found = session.query(PublisherModel).filter(PublisherModel.id == publisher_id).first()
        if publisher_found is None:
            raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher_found


# Create new publisher
@app.post("/publisher/", response_model=PublisherSchema)
async def create_publisher(publisher_create: PublisherSchema):
    with db_session() as session:
        publisher_found = PublisherModel(**publisher_create.dict())
        session.add(publisher_found)
        session.commit()
        session.refresh(publisher_found)
    return publisher_found


# Update publisher based on ID
@app.put("/publisher/{publisher_id}", response_model=PublisherSchema)
async def update_publisher(publisher_id: str, publisher_update: PublisherSchema):
    with db_session() as session:
        publisher_found = session.query(PublisherModel).filter(PublisherModel.id == publisher_id).first()
        if publisher_found is None:
            raise HTTPException(status_code=404, detail="Publisher not found")
        publisher_found.name = publisher_update.name
        publisher_found.address = publisher_update.address
        session.commit()
        session.refresh(publisher_found)
    return publisher_found


# Delete publisher based on ID
@app.delete("/publisher/{publisher_id}", response_model=PublisherSchema)
async def delete_publisher(publisher_id: str):
    with db_session() as session:
        publisher_found = session.query(PublisherModel).filter(PublisherModel.id == publisher_id).first()
        if publisher_found is None:
            raise HTTPException(status_code=404, detail="Publisher not found")
        session.delete(publisher_found)
        session.commit()
        session.refresh(publisher_found)
    return publisher_found


# Get all current library branches
@app.get("/library/", response_model=List[LibraryBranchSchema])
async def get_all_libraries():
    with db_session() as session:
        libraries = session.query(LibraryBranchModel).all()
    return libraries


# Get library branch based on ID
@app.get("/library/{library_id}", response_model=LibraryBranchSchema)
async def get_library_by_id(library_id: str):
    with db_session() as session:
        library_found = session.query(LibraryBranchModel).filter(LibraryBranchSchema.id == library_id).first()
        if library_found is None:
            raise HTTPException(status_code=404, detail="Library not found")
    return library_found


# Create new library branch
@app.post("/library/", response_model=LibraryBranchSchema)
async def create_library(library_create: LibraryBranchSchema):
    with db_session() as session:
        library_found = LibraryBranchModel(**library_create.dict())
        session.add(library_found)
        session.commit()
        session.refresh(library_found)
    return library_found


# Update library branch based on ID
@app.put("/library/{library_id}", response_model=LibraryBranchSchema)
async def update_library(library_id: str, library_update: LibraryBranchSchema):
    with db_session() as session:
        library_found = session.query(LibraryBranchModel).filter(LibraryBranchModel.id == library_id).first()
        if library_found is None:
            raise HTTPException(status_code=404, detail="Library not found")
        library_found.name = library_update.name
        library_found.address = library_update.address
        session.commit()
        session.refresh(library_found)
    return library_found


# Delete library branch based on ID
@app.delete("/library/{library_id}", response_model=LibraryBranchSchema)
async def delete_library(library_id: str):
    with db_session() as session:
        library_found = session.query(LibraryBranchModel).filter(LibraryBranchModel.id == library_id).first()
        if library_found is None:
            raise HTTPException(status_code=404, detail="Library not found")
        session.delete(library_found)
        session.commit()
        session.refresh(library_found)
    return library_found


# Get all current books
@app.get("/book/", response_model=List[BookSchema])
async def get_all_books():
    with db_session() as session:
        books = session.query(BookModel).all()
    return books


# Get book based on ID
@app.get("/book/{book_id}", response_model=BookSchema)
async def get_book_by_id(book_id: str):
    with db_session() as session:
        book_found = session.query(BookModel).filter(BookModel.id == book_id).first()
        if book_found is None:
            raise HTTPException(status_code=404, detail="Book not found")
    return book_found


# Create new book
@app.post("/book/", response_model=BookSchema)
async def create_book(book_create: BookSchema):
    with db_session() as session:
        book_found = BookModel(**book_create.dict())
        session.add(book_found)
        session.commit()
        session.refresh(book_found)
    return book_found


# Update book based on ID
@app.put("/book/{book_id}", response_model=BookSchema)
async def update_book(book_id: str, book_update: BookSchema):
    with db_session() as session:
        book_found = session.query(BookModel).filter(BookModel.id == book_id).first()
        if book_found is None:
            raise HTTPException(status_code=404, detail="Book not found")
        book_found.title = book_update.title
        book_found.publication_date = book_update.publication_date
        session.commit()
        session.refresh(book_found)
    return book_found


# Delete book based on ID
@app.delete("/book/{book_id}", response_model=BookSchema)
async def delete_book(book_id: str):
    with db_session() as session:
        book_found = session.query(BookModel).filter(BookModel.id == book_id).first()
        if book_found is None:
            raise HTTPException(status_code=404, detail="Book not found")
        session.delete(book_found)
        session.commit()
        session.refresh(book_found)
    return book_found
