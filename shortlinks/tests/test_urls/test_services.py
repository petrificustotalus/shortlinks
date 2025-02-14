from unittest.mock import patch

from shortlinks.database import SessionLocal
from shortlinks.models import URL
from shortlinks.urls.services import URLCreator

db = SessionLocal()

def test_create_url():
    existing_url = URL(target_url="https://www.youtube.com/", key="AgH690a")
    db.add(existing_url)
    db.commit()
    with patch("shortlinks.urls.services.create_random_key") as random_key:
        random_key.side_effect = ["AgH690a", "hgfD09a", 'ba23z09']
        url = URLCreator.create(7, "https://www.google.com/", 3, db)    
    
    assert url.key == "hgfD09a"