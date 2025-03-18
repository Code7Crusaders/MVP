import { useState } from 'react';

function Chatbot() {
  const [count, setCount] = useState(0);

  return (
    <>
      <p>Lesss goooo - conteggio: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>
    </>
  );
}

export default Chatbot;
