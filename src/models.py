from sqlmodel import SQLModel, Field, create_engine,Session
from typing import Annotated, List
from fastapi import Depends
from datetime import date


class Movies(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    movie_name: str
    release_date: str
    cast: str
    rating: str
    description: str

sqlite_url = f"sqlite:///movie.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]      



