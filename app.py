import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from models import Base, User
from models.base import Base
from models.users import User

load_dotenv()


def get_engine():
    # Get environment variables
    TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

    if not TURSO_DATABASE_URL or not TURSO_AUTH_TOKEN:
        print("TURSO_DATABASE_URL or TURSO_AUTH_TOKEN is missing")
        DB_URL = "sqlite:///my_test.db"
    else:
        DB_URL = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

    try:
        print(f"Attempting database connection to: {DB_URL}")
        engine = create_engine(
            DB_URL,
            connect_args={"check_same_thread": False, "timeout": 10},
            echo=os.environ.get("DEBUG", "True").lower() in ("true", "1", "t"),
        )
        return engine

    except ConnectionError as err:
        print(f"Database Connection Error: \n\n{err}")


engine = get_engine()  # Create engine instance


def create_db_tables(engine):
    """
    Creates all database tables using the engine.
    """
    with engine.begin() as conn:
        Base.metadata.create_all(conn)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_user(name, email):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)  # Optional: To retrieve the generated ID after insert
        return user


def get_all_users():
    with SessionLocal() as session:
        users = session.query(User).all()
        return users


if __name__ == "__main__":
    create_db_tables(engine)
    INPUT_MESSAGE = os.environ.get("INPUT_MESSAGE")
    print(create_user(name=f"{INPUT_MESSAGE}", email="gha@github.com"))
    print("SELECT all data \n\n")
    results = get_all_users()
    for item in results:
        print(f"{item}")
