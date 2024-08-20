import {Table} from "@radix-ui/themes"
import {Investor} from "@/types"
import "@radix-ui/themes/styles.css"

interface Props {
  investors: Investor[]
  selectInvestorName?: (investorName: string) => void
  selectCommitmentAssetClass?: (commitmentAssetClass: string) => void
}

export default function InvestorTable(props: Props) {
  const handleSelectedInvestorName = async (investor: Investor) => {
    if (props.selectInvestorName) props.selectInvestorName(investor.investorName)
  }

  const handleSelectedCommitmentAssetClass = async (investor: Investor) => {
    if (props.selectCommitmentAssetClass) props.selectCommitmentAssetClass(investor.commitmentAssetClass)
  }

  return (
    <Table.Root layout="auto" size="1">
      <Table.Header>
        <Table.Row>
          <Table.ColumnHeaderCell align="left">ID</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Investor Name</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Investory Type</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Investor Country</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Investor Date Added</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Investor Last Updated</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Commitment Asset Class</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Commitmment Amount</Table.ColumnHeaderCell>
          <Table.ColumnHeaderCell align="left">Commitmment Currency</Table.ColumnHeaderCell>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {props.investors.map(investor => {
          return (
            <Table.Row key={investor.id}>
              <Table.RowHeaderCell>{investor.id}</Table.RowHeaderCell>
              <Table.Cell data-testid={investor.investorName} onClick={() => handleSelectedInvestorName(investor)}>
                {investor.investorName}
              </Table.Cell>
              <Table.Cell>{investor.investoryType}</Table.Cell>
              <Table.Cell>{investor.investorCountry}</Table.Cell>
              <Table.Cell>{investor.investorDateAdded}</Table.Cell>
              <Table.Cell>{investor.investorLastUpdated}</Table.Cell>
              <Table.Cell
                data-testid={investor.commitmentAssetClass}
                onClick={() => handleSelectedCommitmentAssetClass(investor)}
              >
                {investor.commitmentAssetClass}
              </Table.Cell>
              <Table.Cell>{investor.commitmentAmount}</Table.Cell>
              <Table.Cell>{investor.commitmentCurrency}</Table.Cell>
            </Table.Row>
          )
        })}
      </Table.Body>
    </Table.Root>
  )
}
