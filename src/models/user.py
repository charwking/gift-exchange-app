from sqlalchemy import Column, Integer, String
from src.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=80))
