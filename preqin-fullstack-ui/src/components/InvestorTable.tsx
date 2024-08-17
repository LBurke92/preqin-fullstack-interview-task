import {useState, useEffect} from "react"

const {VITE_PREQIN_API_SERVER} = import.meta.env

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
  const [investors, setInvestors] = useState<Investor[]>([])
  useEffect(() => {
    const fetchData = async () => {
      const investors = await fetch(VITE_PREQIN_API_SERVER || "")
      const json = await investors.json()
      setInvestors(json)
    }

    try {
      fetchData()
    } catch (error) {
      console.log(error)
    }
  }, [])

  return (
    <table>
      <tbody>
        {investors.map(investor => {
          return (
            <tr key={investor.id}>
              <td>{investor.id}</td>
              <td>{investor.investorName}</td>
              <td>{investor.investoryType}</td>
              <td>{investor.investorCountry}</td>
              <td>{investor.investorDateAdded}</td>
              <td>{investor.investorLastUpdated}</td>
              <td>{investor.commitmentAssetClass}</td>
              <td>{investor.commitmentAmount}</td>
              <td>{investor.commitmentCurrency}</td>
            </tr>
          )
        })}
      </tbody>
    </table>
  )
}
