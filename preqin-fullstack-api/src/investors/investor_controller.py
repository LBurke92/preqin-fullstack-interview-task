from sqlalchemy import create_engine, Column, String, Integer, DATE, select

from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

Base = declarative_base()


class Investor(Base):
    __tablename__ = "investor"
    id = Column("id", Integer, primary_key=True)
    investorName = Column("Investor Name", String)
    investoryType = Column("Investory Type", String)
    investorCountry = Column("Investor Country", String)
    investorDateAdded = Column("Investor Date Added", DATE)
    investorLastUpdated = Column("Investor Last Updated", DATE)
    commitmentAssetClass = Column("Commitment Asset Class", String)
    commitmentAmount = Column("Commitment Amount", Integer)
    commitmentCurrency = Column("Commitment Currency", String)

    def __init__(
        self,
        id,
        investorName,
        investoryType,
        investorCountry,
        investorDateAdded,
        investorLastUpdated,
        commitmentAssetClass,
        commitmentAmount,
        commitmentCurrency,
    ):
        self.id = id
        self.investorName = investorName
        self.investoryType = investoryType
        self.investorCountry = investorCountry
        self.investorDateAdded = investorDateAdded
        self.investorLastUpdated = investorLastUpdated
        self.commitmentAssetClass = commitmentAssetClass
        self.commitmentAmount = commitmentAmount
        self.commitmentCurrency = commitmentCurrency

    def __repr__(self) -> str:
        # return f"({self.id}, {self.investorName})"
        return f"({self.id}) {self.investorName}, {self.investoryType}, {self.investorCountry}, ({self.investorDateAdded}, {self.investorLastUpdated}) ({self.commitmentAssetClass}, {self.commitmentAmount}, {self.commitmentCurrency})"


engine = create_engine("sqlite+pysqlite:///preqin.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# Creates all classes as tables
def create_tables():
    Base.metadata.create_all(bind=engine)


# Drops all tables defined by all classes
def drop_tables():
    Base.metadata.drop_all(bind=engine)


# Reads the csv file to import data into table
def import_csv_to_table(file_name):
    # file_name = "data.csv"
    df = pd.read_csv(file_name)
    df.to_sql(
        con=engine,
        index_label="id",
        name=Investor.__tablename__,
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


def select_all():
    results = session.query(Investor).all()
    for investor in results:
        print(investor)

    return results


def select_by_investor_name(investor_name: str):
    stmt = select(Investor).where(Investor.investorName == investor_name)

    for investor in session.scalars(stmt):
        print(f"{investor}")

    return session.scalars(stmt)


if __name__ == "__main__":
    print("running main")
    select_all()
    select_by_investor_name("Mjd Jedi fund")
