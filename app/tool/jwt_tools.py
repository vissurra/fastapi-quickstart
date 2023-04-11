import jwt

SECRET = 'U196ELSYqaNK8g9YL9B734h01qvtM5ly'


def encode(payload):
    return jwt.encode(payload, SECRET, algorithm='HS256')


def decode(token) -> dict:
    return jwt.decode(token, SECRET, algorithms='HS256')
