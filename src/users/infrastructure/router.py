from fastapi import APIRouter, Body, Path

from src.users.application.dto import RegisterUserDto, UserDto
from src.users.application.follow_user import FollowUserUserCase
from src.users.application.list_users import ListUsersUseCase
from src.users.application.signup_user import SignInUserUserCase
from src.users.infrastructure.database.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository

router = APIRouter()
router.tags = ['Users']


@router.get(
    path='/',
    response_model=list[UserDto],
    status_code=200,
    description='List all users.'
)
def index():
    list_users = ListUsersUseCase(SqlAlchemyUserRepository())
    return list_users.execute()


@router.post(
    path='/sign-up',
    response_model=UserDto,
    status_code=201,
)
def sign_up(new_user: RegisterUserDto = Body(...)):
    """Register a new user.
        Register a new user in this twitter clone.

        :param new_user: RegisterUserDto data.
        :return: UserEntity UserBase.
    """
    register_user = SignInUserUserCase(SqlAlchemyUserRepository())
    return register_user.execute(new_user)


@router.put(
    path='{user_id}/follows/{followed_id}',
    response_model=UserDto,
    status_code=200,
)
def follow(user_id: str = Path(...), followed_id: str = Path(...)):
    follow_user = FollowUserUserCase(SqlAlchemyUserRepository())
    return follow_user.execute(user_id, followed_id)