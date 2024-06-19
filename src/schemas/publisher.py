from datetime import datetime

from myapp import BaseModel


class CustomerSchema(BaseModel):
    name: str | None = None
    publisher: str | None = None
