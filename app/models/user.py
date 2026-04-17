from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    phone = Column(String)
    hashed_password = Column(String)
    role = Column(String, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="owner")