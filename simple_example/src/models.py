from pydantic import BaseModel


class Person(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    gender: str
