from faker import Faker

from src.users.application.dto import RegisterUserDto


class RegisterUserDtoMotherObject:
    @staticmethod
    def apply(
        username: str,
        email: str,
        profile_name: str,
        birthdate,
        password: str,
        profile_description: str
    ):
        return RegisterUserDto(
            username=username,
            email=email,
            profile_name=profile_name,
            birthdate=birthdate,
            password=password,
            profile_description=profile_description
        )

    @staticmethod
    def random():
        fake = Faker()
        return RegisterUserDto(
            username=fake.user_name(),
            email=fake.email(),
            profile_name=fake.name(),
            birthdate=fake.date_of_birth(minimum_age=18, maximum_age=100),
            password=fake.password(),
            profile_description=fake.text()
        )
