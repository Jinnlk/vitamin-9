import React, { useState } from "react";

function App() {
  const [quote, setQuote] = useState("");

  const fetchQuote = async () => {
    const response = await fetch("https://your-backend-url/quote");
    const data = await response.json();
    setQuote(data.quote);
  };

  return (
    <div>
      <h1>Quote of the Day</h1>
      <p>{quote}</p>
      <button onClick={fetchQuote}>Get a New Quote</button>
    </div>
  );
}

export default App;
