import unittest
from unittest.mock import MagicMock

from src.users.application.signup_user import SignInUserUserCase
from src.users.domain.user_entity import UserEntity
from src.users.domain.user_repository import UserRepository
from tests.users.domain.register_user_dto_mother_object import RegisterUserDtoMotherObject


class TestSignUp(unittest.TestCase):
    def test_signup_user(self):
        random_user = RegisterUserDtoMotherObject.random()
        repo = MagicMock(UserRepository)
        use_case = SignInUserUserCase(repo)

        response = use_case.execute(random_user)
        assert response is not None
        assert isinstance(response, UserEntity)
        repo.save.assert_called_once()
