import secrets


def generate_secret_token():
    """Генерирует секретный токен длиной 256 символов."""
    token = secrets.token_hex(128)
    if len(token) < 256 or len(token) > 256:
        generate_secret_token()
    return token
