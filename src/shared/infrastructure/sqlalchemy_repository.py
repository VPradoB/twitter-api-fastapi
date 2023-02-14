from src.shared.domain.repositories import IRepository
from src.shared.infrastructure.database import Database


class SQLAlchemyRepository(IRepository):
    db = Database.session

    def get(self, id):
        pass

    def save(self, entity):
        self.db.add(entity)
        self.db.commit()
        return entity
