from pydantic import BaseModel
from datetime import date


class InvestorBase(BaseModel):
    investorName: str
    investoryType: str
    investorCountry: str
    investorDateAdded: date
    investorLastUpdated: date
    commitmentAssetClass: str
    commitmentAmount: int
    commitmentCurrency: str


class InvestorCreate(InvestorBase):
    pass


class Investor(InvestorBase):
    id: int

    class Config:
        from_attributes = True
