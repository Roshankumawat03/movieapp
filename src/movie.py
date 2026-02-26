from fastapi import Depends, APIRouter, Body
from sqlmodel import select
from src.models import SessionDep,Movies

movie_route = APIRouter(tags=["movie_management"])


@movie_route.get("/")
def home(db: SessionDep):
    statement = select(Movies)
    movies = db.exec(statement).all()
    return movies


@movie_route.post("/create_movie")
def create_movie(db: SessionDep, data = Body(...)):
    data_for_entry = Movies(
        movie_name=data.get("movie_name"),
        release_date=data.get("release_date"),
        cast=data.get("cast"),
        rating=data.get("rating"),
        description=data.get("description")
    )
    db.add(data_for_entry)
    db.commit()
    return "User created done."
