import InvestorTable from "@/components/InvestorTable"
import {Button, Flex} from "@radix-ui/themes"
import {useLoaderData, useNavigate} from "react-router-dom"
import {Investor} from "@/types"

export default function CommitmentAssetClassDetailsPage() {
  const navigate = useNavigate()
  const investors = useLoaderData() as Investor[]

  const handleGoBack = () => {
    navigate("/")
  }

  return (
    <>
      <Flex justify="between" align="center">
        <h1>Investments by Commitment Asset Class</h1>
        <Button onClick={handleGoBack}>Go back </Button>
      </Flex>
      <InvestorTable investors={investors} />
    </>
  )
}
