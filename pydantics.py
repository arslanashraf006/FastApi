#Pydantic is a Python library to perform data validation.
from pydantic import BaseModel, EmailStr

class person(BaseModel):
    name : str
    age : int
    email : EmailStr

all = person(name ="Ali",age = "25",email = "ali@ameer.com")
print(all)