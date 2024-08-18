from sqlalchemy import String, Integer, DATE
from sqlalchemy.orm import Session
import pandas as pd
from .database import SessionLocal, engine

from . import models, schemas, database


def get_investor_by_investor_name(db: Session, investor_name: str):
    return db.query(models.Investor).filter(
        models.Investor.investorName == investor_name
    )


def get_investor_by_commitment_asset_class(db: Session, commitment_asset_class: str):
    return db.query(models.Investor).filter(
        models.Investor.commitmentAssetClass == commitment_asset_class
    )


def get_all_investors(db: Session, skip: int = 0, limit: int = 300):
    return db.query(models.Investor).offset(skip).limit(limit).all()


def create_investor(db: Session, investor: schemas.InvestorCreate):
    db_investor = models.Investor(**investor.model_dump())
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor


def create_investors_from_csv(file_name):
    df = pd.read_csv(file_name)
    df.to_sql(
        con=database.engine,
        index_label="id",
        name=models.Investor.__tablename__,
        if_exists="replace",
        dtype={
            "index": Integer,
            "investorName": String,
            "investoryType": String,
            "investorCountry": String,
            "investorDateAdded": DATE,
            "investorLastUpdated": DATE,
            "commitmentAssetClass": String,
            "commitmentAmount": Integer,
            "commitmentCurrency": String,
        },
    )


if __name__ == "__main__":
    db = SessionLocal()
    create_investors_from_csv("./investors/data.csv")
