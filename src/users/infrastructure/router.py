from fastapi import APIRouter, Body

from src.users.application.dto import RegisterUserDto, UserDto

from src.users.application.registerUser import RegisterUserUseCase
from src.users.infrastructure.database.repositories.sqlite_user_repository import SqliteUserRepository
router = APIRouter()
router.tags = ['Users']

@router.get('/')
def index():
    pass

@router.post(
    path='/sign-up',
    response_model=UserDto,
    status_code=201
)
def sign_up(new_user: RegisterUserDto = Body(...)):
    """Register a new user.
        Register a new user in this twitter clone.

        :param new_user: RegisterUserDto data.
        :return: UserEntity UserBase.
    """
    register_user = RegisterUserUseCase(SqliteUserRepository())
    return register_user.execute(new_user)

    pass
