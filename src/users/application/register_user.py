import os

from src.users.application.dto import RegisterUserDto
from src.users.domain.user_entity import UserEntity
import logging
logger = logging.getLogger(os.getenv('LOGGER_NAME'))

class RegisterUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, new_user: RegisterUserDto):
        """Register a new user."""
        try:
            user: UserEntity = UserEntity.register(**new_user.__dict__, repository=self.user_repository)
            logger.info(f'User {user.username} registered successfully.')
            return user
        except Exception as e:
            logger.error(f'Error registering user: {e}')
            raise e
