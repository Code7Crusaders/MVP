import { useState } from 'react'
import '../css/style.css'
import {MainView} from "../components/MainView"

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <MainView></MainView>
      <p>Ce l'abbiamo fatta!</p>
    </>
  )
}

export default App