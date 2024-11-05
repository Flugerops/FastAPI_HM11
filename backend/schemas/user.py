from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(examples="John Doe")
    email: str = Field(examples="johndoe@gmail.com")


class UserInDB(User):
    hashed_password: str
