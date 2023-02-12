from src.users.domain.user_entity import IUserRepository


class SqliteUserRepository(IUserRepository):
    """UserEntity repository."""

    def get_following(self, user_id):
        pass

    def get_profile_picture(self, user_id):
        pass

    def get(self, id):
        pass

    def get_followers(self, user_id):
        pass

    def get_by_email(self, email):
        pass

    def save(self, user):
        pass

    def find_by_email(self, email):
        pass

    def find_by_id(self, id):
        pass

    def find_by_username(self, username):
        pass
