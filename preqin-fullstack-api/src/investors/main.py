from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from . import crud, models, schemas
from .database import SessionLocal, engine
from .helpers import investor_filter_and_sort

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Future considerations for an ORM are Tortoise ORM (async by default) or PeeWee (fast, powerful)
# https://www.infoworld.com/article/2335270/6-orms-for-every-database-powered-python-app.html
@app.get("/", response_model=list[schemas.Investor])
def read_investors(db: Session = Depends(get_db), skip: int = 0, limit: int = 300):
    results = crud.get_all_investors(db, skip, limit)
    # investor_filter_and_sort(results)
    return results


@app.get("/investor/{investor_name}", response_model=list[schemas.Investor])
def read_investor_by_investor_name(
    db: Session = Depends(get_db),
    investor_name: str = "",
):
    results = crud.get_investor_by_investor_name(db, investor_name)
    return results


@app.get(
    "/commitment-asset-class/{commitment_asset_class}",
    response_model=list[schemas.Investor],
)
def read_investor_by_commitment_asset_class(
    db: Session = Depends(get_db),
    commitment_asset_class: str = "",
):
    results = crud.get_investor_by_commitment_asset_class(db, commitment_asset_class)
    return results


@app.get(
    "/commitment-asset-class/{commitment_asset_class}",
    response_model=list[schemas.Investor],
)
def read_investors(db: Session = Depends(get_db), skip: int = 0, limit: int = 300):
    results = crud.get_all_investors(db, skip, limit)
    investor_filter_and_sort(results)
    return results
