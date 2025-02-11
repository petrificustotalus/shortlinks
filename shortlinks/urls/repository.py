from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..errors import NotUniqueKey
from ..models import URL


class URLRepository:
    @classmethod
    def create(cls, target_url: str, key: str, db: Session):
        new_url = URL(target_url=target_url, key=key)
        db.add(new_url)
        try:
            db.commit()
            db.refresh(new_url)
        except IntegrityError:
            db.rollback()
            raise NotUniqueKey(f"Key {key} already exists")
        return new_url

    @classmethod
    def get_by_key(cls, key: str, db: Session):
        url = db.query(URL).filter(URL.key == key).first()
        return url

    @classmethod
    def get_by_target_url(cls, target_url: str, db: Session):
        url = db.query(URL).filter(URL.target_url == target_url).first()
        return url
