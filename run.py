from src import models, movie
from fastapi import FastAPI

app = FastAPI()

app.include_router(movie.movie_route)