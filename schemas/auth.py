from pydantic import BaseModel

class RegisterRequest(BaseModel):
    email: str
    username: str
    phone: str
    password: str