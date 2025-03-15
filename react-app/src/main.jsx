import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './css/style.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from './App.jsx'

import store from "react-redux"
import { Provider} from "react-redux"

const router = createBrowserRouter([
  {
    path: "/",
    element: <App></App>
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Provider store={store}>
      <RouterProvider router={router}/>
    </Provider>
  </StrictMode>,
)
