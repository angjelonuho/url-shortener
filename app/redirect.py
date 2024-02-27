from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import get_db
from .models import Url

router = APIRouter()

@router.get("/{shortcode}")
def redirect_to_url(shortcode: str, db: Session = Depends(get_db)):
    db_url = db.query(Url).filter(Url.shortcode == shortcode).first()
    if not db_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shortcode not found")
    return RedirectResponse(url=db_url.url, status_code=302, headers={"Location": db_url.url})
