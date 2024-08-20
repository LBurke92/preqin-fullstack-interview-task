import {render, screen} from "@testing-library/react"
import InvestorTable from "@/components/InvestorTable"
import {mockAllInvestors} from "@/mocks/mockInvestors"

describe("InvestorTable", () => {
  it("matches the DOM snapshot", () => {
    const component = render(<InvestorTable investors={mockAllInvestors} />)

    expect(component).toMatchSnapshot()
  })
  it("displays x", () => {
    render(<InvestorTable investors={mockAllInvestors} />)

    expect(screen.getAllByTestId("Ioo Gryffindor fund")[0]).toBeInTheDocument()
  })
})
