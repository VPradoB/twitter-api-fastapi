from src.users.domain.user import IUserRepository


class UserRepository(IUserRepository):
    """User repository."""

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

    def __init__(self):
        pass

    def save(self, user):
        pass

    def find_by_email(self, email):
        pass

    def find_by_id(self, id):
        pass

    def find_by_username(self, username):
        pass
