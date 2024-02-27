import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Url(Base):
    __tablename__ = "shorten_urls"
    id = Column(Integer, primary_key=True, index=True)
    shortcode = Column(String, index=True, unique=True)
    url = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_redirect_at = Column(DateTime, default=None)
    redirect_count = Column(Integer, default=0)
