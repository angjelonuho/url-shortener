from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Url
from .utils import generate_shortcode

router = APIRouter()

class ShortenRequest(BaseModel):
    url: str
    shortcode: str = None

@router.post("/shorten", status_code=status.HTTP_201_CREATED)
def shorten_url(request: ShortenRequest, db: Session= SessionLocal()):
    if not request.url:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Url not present")
    with db.begin():
        if request.shortcode:
            if db.query(Url).filter(Url.shortcode == request.shortcode).first():
                raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail="Shortcode already in use")
            if not all(c.isalnum() or c== '_' for c in request.shortcode):
                raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail="The provided shortcode is invalid")
        else:
            request.shortcode = generate_shortcode()
        
        db_url=Url(shortcode=request.shortcode, url=request.url)
        db.add(db_url)
        db.commit()
    
    return {"shortcode": request.shortcode}