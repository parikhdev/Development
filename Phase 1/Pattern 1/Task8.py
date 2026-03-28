from pydantic import BaseModel, field_validator, EmailStr, Field, ValidationError
from typing import Optional

class UserSignup(BaseModel):
    username: str = Field(min_length = 3)
    age: int = Field(lt = 120)
    email: EmailStr
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if value < 18:
            raise ValueError("Age should be 18 or older")
        return value
u1 = UserSignup.model_validate({"username": "ali", "age": 25, "email": "ali@gmail.com"})
data = u1.model_dump()
print(u1)
print(data)
data = u1.model_dump(exclude={"email"})
print(data)
try:
    bad_user = UserSignup.model_validate({
        "username": "ab",
        "age": 15,
        "email": "notanemail"
    })
except ValidationError as e:
    print(e)