from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import get_db
from .models import Url

router = APIRouter()

@router.get("/{shortcode}/stats")
def get_shortcode_stats(shortcode: str, db: Session = Depends(get_db)):
    db_url = db.query(Url).filter(Url.shortcode == shortcode).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Shortcode not found")

    return {
        "created": db_url.created_at,
        "lastRedirect": db_url.last_redirect_at,
        "redirectCount": db_url.redirect_count
    }
