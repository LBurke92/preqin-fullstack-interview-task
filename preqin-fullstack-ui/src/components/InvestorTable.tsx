import {useLoaderData, useNavigate} from "react-router-dom"
import {Table} from "@radix-ui/themes"
import "@radix-ui/themes/styles.css"

interface Investor {
  id: number
  investorName: string
  investoryType: string
  investorCountry: string
  investorDateAdded: string
  investorLastUpdated: string
  commitmentAssetClass: string
  commitmentAmount: number
  commitmentCurrency: string
}

export function InvestorTable() {
  const navigate = useNavigate()
  const investors = useLoaderData() as Investor[]

  const handleSelectedInvestorName = async (investor: Investor) => {
    navigate(`investor/${investor.investorName}`)
  }

  const handleSelectedCommitmentAssetClass = async (investor: Investor) => {
    navigate(`commitment-asset-class/${investor.commitmentAssetClass}`)
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
        {investors.map(investor => {
          return (
            <Table.Row key={investor.id}>
              <Table.RowHeaderCell>{investor.id}</Table.RowHeaderCell>
              <Table.Cell onClick={() => handleSelectedInvestorName(investor)}>{investor.investorName}</Table.Cell>
              <Table.Cell>{investor.investoryType}</Table.Cell>
              <Table.Cell>{investor.investorCountry}</Table.Cell>
              <Table.Cell>{investor.investorDateAdded}</Table.Cell>
              <Table.Cell>{investor.investorLastUpdated}</Table.Cell>
              <Table.Cell onClick={() => handleSelectedCommitmentAssetClass(investor)}>
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
