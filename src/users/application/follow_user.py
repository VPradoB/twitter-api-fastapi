from src.users.domain.user_entity import IUserRepository


class FollowUserUserCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_id, followed_id):
        user = self.user_repository.get_by_id(user_id)
        followed = self.user_repository.get_by_id(followed_id)
        return user.follow(followed)
