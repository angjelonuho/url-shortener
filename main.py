from fastapi import FastAPI
from app.shorten import router as shorten_router
from app.redirect import router as redirect_router

app = FastAPI()

app.include_router(shorten_router)
app.include_router(redirect_router)
