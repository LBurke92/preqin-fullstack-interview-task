def test_read_investors(test_client):
    response = test_client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data[0] == {
        "investorName": "Ioo Gryffindor fund",
        "investoryType": "fund manager",
        "investorCountry": "Singapore",
        "investorDateAdded": "2000-07-06",
        "investorLastUpdated": "2024-02-21",
        "commitmentAssetClass": "Infrastructure",
        "commitmentAmount": 15000000,
        "commitmentCurrency": "GBP",
        "id": 0,
    }


def test_read_investor_by_investor_name(test_client):
    response = test_client.get("/investor/Ioo Gryffindor fund")

    assert response.status_code == 200

    data = response.json()

    assert data[0] == {
        "investorName": "Ioo Gryffindor fund",
        "investoryType": "fund manager",
        "investorCountry": "Singapore",
        "investorDateAdded": "2000-07-06",
        "investorLastUpdated": "2024-02-21",
        "commitmentAssetClass": "Infrastructure",
        "commitmentAmount": 15000000,
        "commitmentCurrency": "GBP",
        "id": 0,
    }


def test_read_investor_by_commitment_asset_class(test_client):
    response = test_client.get("/commitment-asset-class/Infrastructure")

    assert response.status_code == 200

    data = response.json()

    assert data[0] == {
        "investorName": "Ioo Gryffindor fund",
        "investoryType": "fund manager",
        "investorCountry": "Singapore",
        "investorDateAdded": "2000-07-06",
        "investorLastUpdated": "2024-02-21",
        "commitmentAssetClass": "Infrastructure",
        "commitmentAmount": 15000000,
        "commitmentCurrency": "GBP",
        "id": 0,
    }
