from sqlmodel import create_engine, Session

sqlite_url = "sqlite:///./juegos.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})


def get_db():
    with Session(engine) as session:
        yield session