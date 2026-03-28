from pydantic import BaseModel, field_validator, EmailStr, Field
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
u1 = UserSignup(username="ali", age=25, email="ali@gmail.com")
print(u1)

# u2 = UserSignup(username="ab", age=15, email="x@x.com")
# print(u2)