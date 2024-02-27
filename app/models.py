from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Url(Base):
    __tablename__ = "shorten_urls"
    id = Column(Integer, primary_key=True, index=True)
    shortcode = Column(String, index=True, unique=True)
    url = Column(String, index=True)
    created_at = Column(DateTime)
