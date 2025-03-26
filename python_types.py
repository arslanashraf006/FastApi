from datetime import datetime
#Pydantic is a Python library to perform data validation.
from pydantic import BaseModel

def full_name(fname : str, lname : str):
    fname = fname.capitalize()
    return fname + " " + lname

firstname = "ali"
lastname = "ameer"

print(full_name(firstname, lastname))

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)