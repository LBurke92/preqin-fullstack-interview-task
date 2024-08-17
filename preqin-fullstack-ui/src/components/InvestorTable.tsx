import {useState, useEffect} from "react"

const {VITE_PREQIN_API_SERVER} = import.meta.env

interface Investor {
  message: string
}

// interface Investors {
//   id: number
//   investor_name: string
//   investory_type: string
//   investor_country: string
//   investor_date_added: Date
//   investor_last_updated: Date
//   commitment_asset_class: string
//   commitment_amount: number
//   commitment_currency: string
// }

export function InvestorTable() {
  const [investors, setInvestors] = useState<Investor>({} as Investor)
  useEffect(() => {
    fetch(VITE_PREQIN_API_SERVER || "")
      .then(res => {
        return res.json()
      })
      .then(data => {
        setInvestors(data)
      })
  }, [])

  return (
    <table>
      <tbody>
        <tr>
          <td>Hi</td>
          <td>Bye</td>
          <td>{investors.message}</td>
        </tr>
      </tbody>
    </table>
  )
}
