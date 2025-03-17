import { useState } from 'react'
import MainView from '../components/MainView'

function login() {
  const [count, setCount] = useState(0)

  return (
    <>    
      <MainView></MainView>
    </>
  )
}

export default login