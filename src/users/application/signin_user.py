from src.users.domain.user_entity import IUserRepository, UserEntity


class UserNotFound(Exception):
    pass


class InvalidPassword(Exception):
    pass


class SingInUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> UserEntity:
        user: UserEntity = self.user_repository.get_by_email(email)
        if not user:
            raise UserNotFound()

        if not user.check_password(password):
            raise InvalidPassword()

        return user
