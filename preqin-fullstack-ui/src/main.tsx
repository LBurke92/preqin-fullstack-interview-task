import * as React from "react"
import * as ReactDOM from "react-dom/client"
import {createBrowserRouter, RouterProvider} from "react-router-dom"
import {Theme} from "@radix-ui/themes"

import RootPage from "@/routes/rootPage"
import CommitmentAssetClassPage from "@/routes/commitmentAssetClassPage"
import InvestorDetailsPage from "@/routes/investorDetailsPage"

import "@radix-ui/themes/styles.css"
import "./main.css"

const {VITE_PREQIN_API_SERVER} = import.meta.env

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootPage />,
    loader: async ({request}) => {
      return fetch(`${VITE_PREQIN_API_SERVER}`, {signal: request.signal})
    },
    errorElement: <div>Sorry, something has gone wrong</div>
  },
  {
    path: "/commitment-asset-class/:commitmentAssetClass",
    element: <CommitmentAssetClassPage />,
    loader: async ({request, params}) => {
      return fetch(`${VITE_PREQIN_API_SERVER}/commitment-asset-class/${params.commitmentAssetClass}`, {
        signal: request.signal
      })
    },
    errorElement: <div>Sorry, something has gone wrong</div>
  },
  {
    path: "/investor/:investorName",
    element: <InvestorDetailsPage />,
    loader: async ({request, params}) => {
      return fetch(`${VITE_PREQIN_API_SERVER}/investor/${params.investorName}`, {signal: request.signal})
    },
    errorElement: <div>Sorry, something has gone wrong</div>
  }
])

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Theme
      accentColor="gold"
      grayColor="sand"
      panelBackground="translucent"
      scaling="100%"
      radius="full"
      hasBackground={true}
    >
      <RouterProvider router={router} />
    </Theme>
  </React.StrictMode>
)
