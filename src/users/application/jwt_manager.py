from jwt import encode, decode


def create_token(data: dict, secret):
    return encode(payload=data, key=secret, algorithm='HS256')


def validate_token(token: str, secret: str):
    return decode(token, key=secret, algorithms=['HS256'])
