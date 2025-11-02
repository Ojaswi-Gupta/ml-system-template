# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
# from app.core.config import settings  # Import your settings

# # 1. Use the .database_url property from your settings
# # This is cleaner than rebuilding the URL here.
# # It also ensures you use the correct driver, like 'postgresql+psycopg2'.
# engine = sqlalchemy.create_engine(settings.database_url)

# # 2. Create the SessionLocal factory
# # These are the defaults, but being explicit is good practice.
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # 3. Create the dependency for your API endpoints
# def get_db():
#     """
#     FastAPI dependency to create and manage a database session.
#     - Creates a session from SessionLocal() for a request.
#     - 'yields' the session to the endpoint.
#     - 'finally' closes the session after the request is done.
#     """
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session  # <-- 1. Import Session
from app.core.config import settings
from typing import Generator  # <-- 2. Import Generator


engine = sqlalchemy.create_engine(settings.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 3. Add the type hints for the function and the 'db' variable
def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
