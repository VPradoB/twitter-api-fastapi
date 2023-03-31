from src.users.domain.user_entity import IUserRepository


class ListUsersUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.get_all()
