from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str
    
class Standard(BaseModel):
    message: str

class ErrorOutput(Standard):
    detail: str