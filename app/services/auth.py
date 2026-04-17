from app.repositories.user import UserRepository

class AuthService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def register(self, data):
        return self.repo.create(**data.dict())