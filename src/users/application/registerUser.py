from src.users.application.dto import RegisterUserDto
from src.users.domain.user import User

class RegisterUserUseCase:
    def __init__(self, user_repository):
        super()
        self.user_repository = user_repository

    def execute(self, new_user: RegisterUserDto):
        user = User(
            username=new_user.username,
            email=new_user.email,
            profile_name=new_user.profile_name,
            birthdate=new_user.birthdate,
            password=User.hash_password(new_user.password),
            repository=self.user_repository
        )
        user.save()
        return user.without_password()
