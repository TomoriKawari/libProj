from datetime import datetime
from myapp import BaseModel


class CustomerSchema(BaseModel):
    name: str | None = None
    birthdate: datetime | None = None
