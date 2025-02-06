import { useEffect, useState } from "react";
import { fetchBackendMessage } from "./api/backend";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const getMessage = async () => {
      const backendMessage = await fetchBackendMessage();
      setMessage(backendMessage);
    };
    getMessage();
  }, []);

  return (
    <div>
      <h1>AI Music Chatbot Frontend</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
