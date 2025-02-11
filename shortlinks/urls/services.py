import secrets
import string

from sqlalchemy.orm import Session

from ..errors import KeyGenerationError, NotUniqueKey
from .repository import URLRepository


class URLCreator:
    @classmethod
    def create(cls, key_length: int, target_url: str, attempts: int, db: Session):
        if attempts >= 1:
            key = create_random_key(key_length)
            try:
                short_url = URLRepository.create(target_url, key, db)
                return short_url
            except NotUniqueKey:
                attempts -= 1
                URLCreator.create(key_length, target_url, attempts, db)
        raise KeyGenerationError()


def create_random_key(length: int) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))
