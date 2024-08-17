from sqlalchemy import Column, String, Integer, DATE
from .database import Base


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
