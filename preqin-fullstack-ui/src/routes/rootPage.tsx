import InvestorTable from "@/components/InvestorTable"
import {useLoaderData, useNavigate} from "react-router-dom"
import {Investor} from "@/types"

export default function RootPage() {
  const navigate = useNavigate()
  const investors = useLoaderData() as Investor[]

  const handleSelectedInvestorName = async (investorName: string) => {
    navigate(`investor/${investorName}`)
  }

  const handleSelectedCommitmentAssetClass = async (commitmentAssetClass: string) => {
    navigate(`commitment-asset-class/${commitmentAssetClass}`)
  }

  console.log(investors.slice(0, 10))

  return (
    <>
      <h1>Preqin Investors</h1>
      <InvestorTable
        investors={investors}
        selectInvestorName={handleSelectedInvestorName}
        selectCommitmentAssetClass={handleSelectedCommitmentAssetClass}
      />
    </>
  )
}
