import validators
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from ..config import get_settings
from ..database import get_db
from ..errors import KeyGenerationError
from .repository import URLRepository
from .schemas import URLBase, URLInfo, URLStats
from .services import URLCreator

router = APIRouter(prefix="/url", tags=["URLS"])
settings = get_settings()
key_length = settings.key_length
attempts = settings.attempts


@router.put("/", response_model=URLInfo, status_code=status.HTTP_200_OK)
def create_url(url: URLBase, response: Response, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Provided URL is invalid")

    short_url = URLRepository.get_by_target_url(url.target_url, db)
    if not short_url:
        response.status_code = status.HTTP_201_CREATED
        try:
            short_url = URLCreator.create(key_length, url.target_url, attempts, db)
        except KeyGenerationError:
            # logging
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unable to generate shortened url",
            )

    base_url = settings.base_url
    endpoint_url = router.url_path_for("forward target", url_key=short_url.key)
    e = base_url + endpoint_url
    resp = URLInfo(**{"url": e})
    return resp


@router.get(
    "/{url_key}",
    name="forward target",
)
def forward_to_target_url(url_key: str, db: Session = Depends(get_db)):
    db_url = URLRepository.get_by_key(url_key, db)
    if db_url:
        db_url.visits += 1
        db.add(db_url)
        db.commit()
        return RedirectResponse(db_url.target_url)
    else:
        raise HTTPException(status_code=404, detail="Provided URL is invalid")


@router.get("/{url_key}/info", response_model=URLStats, status_code=status.HTTP_200_OK)
def stats(url_key: str, db: Session = Depends(get_db)):
    db_url = URLRepository.get_by_key(url_key, db)
    if db_url:
        return db_url
    else:
        raise HTTPException(status_code=404, detail="Provided URL is invalid")
