from . import models, schemas
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    # Check if id and name already exists
    # Optional, can be removed if unnecessary
    if crud.get_user_by_name(db, name=user.name):
        raise HTTPException(status_code=400, detail="Name is already registered")
    if crud.get_user(db, user_id=user.id):
        raise HTTPException(status_code=400, detail="Id is already in use")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
