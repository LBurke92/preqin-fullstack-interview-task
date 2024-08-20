import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker, declarative_base
from investors.database import engine, Base
from investors.main import app, get_db


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    """Create a new database session with a rollback at the end of the test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """Create a test client that uses the override_get_db fixture to return a session."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def investor_payload():
    """Generate an updated investor payload."""
    return [
        {
            "investorName": "Ioo Gryffindor fund",
            "investoryType": "fund manager",
            "investorCountry": "Singapore",
            "investorDateAdded": "2000-07-06",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Infrastructure",
            "commitmentAmount": 15000000,
            "commitmentCurrency": "GBP",
            "id": 0,
        },
        {
            "investorName": "Ibx Skywalker ltd",
            "investoryType": "asset manager",
            "investorCountry": "United States",
            "investorDateAdded": "1997-07-21",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Infrastructure",
            "commitmentAmount": 31000000,
            "commitmentCurrency": "GBP",
            "id": 1,
        },
        {
            "investorName": "Cza Weasley fund",
            "investoryType": "wealth manager",
            "investorCountry": "United Kingdom",
            "investorDateAdded": "2002-05-29",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Hedge Funds",
            "commitmentAmount": 58000000,
            "commitmentCurrency": "GBP",
            "id": 2,
        },
        {
            "investorName": "Mjd Jedi fund",
            "investoryType": "bank",
            "investorCountry": "China",
            "investorDateAdded": "2010-06-08",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Private Equity",
            "commitmentAmount": 72000000,
            "commitmentCurrency": "GBP",
            "id": 3,
        },
        {
            "investorName": "Mjd Jedi fund",
            "investoryType": "bank",
            "investorCountry": "China",
            "investorDateAdded": "2010-06-08",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Natural Resources",
            "commitmentAmount": 1000000,
            "commitmentCurrency": "GBP",
            "id": 4,
        },
        {
            "investorName": "Ibx Skywalker ltd",
            "investoryType": "asset manager",
            "investorCountry": "United States",
            "investorDateAdded": "1997-07-21",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Real Estate",
            "commitmentAmount": 17000000,
            "commitmentCurrency": "GBP",
            "id": 5,
        },
        {
            "investorName": "Ibx Skywalker ltd",
            "investoryType": "asset manager",
            "investorCountry": "United States",
            "investorDateAdded": "1997-07-21",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Real Estate",
            "commitmentAmount": 83000000,
            "commitmentCurrency": "GBP",
            "id": 6,
        },
        {
            "investorName": "Mjd Jedi fund",
            "investoryType": "bank",
            "investorCountry": "China",
            "investorDateAdded": "2010-06-08",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Hedge Funds",
            "commitmentAmount": 28000000,
            "commitmentCurrency": "GBP",
            "id": 7,
        },
        {
            "investorName": "Ibx Skywalker ltd",
            "investoryType": "asset manager",
            "investorCountry": "United States",
            "investorDateAdded": "1997-07-21",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Hedge Funds",
            "commitmentAmount": 85000000,
            "commitmentCurrency": "GBP",
            "id": 8,
        },
        {
            "investorName": "Ioo Gryffindor fund",
            "investoryType": "fund manager",
            "investorCountry": "Singapore",
            "investorDateAdded": "2000-07-06",
            "investorLastUpdated": "2024-02-21",
            "commitmentAssetClass": "Hedge Funds",
            "commitmentAmount": 31000000,
            "commitmentCurrency": "GBP",
            "id": 9,
        },
    ]
