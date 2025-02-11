from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str


class URLInfo(BaseModel):
    url: str


class URLStats(BaseModel):
    key: str
    target_url: str
    visits: int
