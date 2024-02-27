from fastapi import FastAPI
from app.shorten import router as shorten_router
from app.redirect import router as redirect_router
from app.database import Base, engine
#to ensure they are included in metadata
from app.models import Url

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(shorten_router)
app.include_router(redirect_router)
