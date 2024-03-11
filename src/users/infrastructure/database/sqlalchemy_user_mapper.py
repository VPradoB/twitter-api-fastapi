from src.users.domain.user_entity import UserEntity, IUserRepository
from src.users.infrastructure.database.user_table import UserInDB


class UserMapper:
    @classmethod
    def to_entity(cls, user: UserInDB, repository: IUserRepository) -> UserEntity:
        return UserEntity(
            id=user.id,
            email=user.email,
            followers_count=user.followers_count,
            following_count=user.following_count,
            username=user.username,
            profile_name=user.profile_name,
            hashed_password=user.hashed_password,
            profile_description=user.profile_description,
            tweet_count=user.tweet_count,
            profile_picture=user.profile_picture,
            birthdate=user.birthdate,
            repository=repository,
        )

    @classmethod
    def to_database(cls, user: UserEntity) -> UserInDB:
        return UserInDB(
            id=user.id,
            email=user.email,
            followers_count=user.followers_count,
            following_count=user.following_count,
            username=user.username,
            profile_name=user.profile_name,
            hashed_password=user.hashed_password,
            profile_description=user.profile_description,
            tweet_count=user.tweet_count,
            profile_picture=user.profile_picture,
            birthdate=user.birthdate,
        )
