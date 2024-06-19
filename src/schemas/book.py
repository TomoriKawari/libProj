from datetime import datetime

from myapp import BaseModel


class CustomerSchema(BaseModel):
    publication_date: datetime | None = None
    title: str | None = None
