import pytest
from app.models import Url
from app.database import engine, SessionLocal, Base
from sqlalchemy_utils import create_database, database_exists

@pytest.fixture(scope='session')
def setup_database():

    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        existing_url = db.query(Url).filter(Url.shortcode == "test_shortcode").first()
        if not existing_url:
            test_url = Url(url="http://example.com", shortcode="test_shortcode")
            db.add(test_url)
            db.commit()

    yield
