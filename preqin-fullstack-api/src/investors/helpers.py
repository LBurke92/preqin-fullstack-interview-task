from collections import defaultdict
from .schemas import Investor


def investor_filter_and_sort(investors: list[Investor]):

    unique_investors = defaultdict(
        lambda: {
            "investorName": "",
            "investoryType": "",
            "investorCountry": "",
            "investorDateAdded": "",
            "commitmentAmount": 0,
        }
    )

    for investor in investors:
        unique_investors[investor.investorName]["investorName"] = investor.investorName
        unique_investors[investor.investorName][
            "investoryType"
        ] = investor.investoryType
        unique_investors[investor.investorName][
            "investorCountry"
        ] = investor.investorCountry
        unique_investors[investor.investorName][
            "investorDateAdded"
        ] = investor.investorDateAdded
        unique_investors[investor.investorName][
            "commitmentAmount"
        ] += investor.commitmentAmount

    unique_investors = dict(unique_investors)

    # for items in unique_investors.items():
    #     print(items)

    return unique_investors
