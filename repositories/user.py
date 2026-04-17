from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def create(self, email, username, phone, password, role="user"):
        user = User(
            email=email,
            username=username,
            phone=phone,
            hashed_password=hash_password(password),
            role=role
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user