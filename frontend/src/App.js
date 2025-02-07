import React, { useState } from "react";
import ChatInput from "./components/ChatInput";
import ChatResponse from "./components/ChatResponse";

function App() {
  const [chatResponse, setChatResponse] = useState("");

  const handleSend = async (userInput) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_input: userInput }),
      });
      const data = await response.json();
      setChatResponse(data.response || "No response received.");
    } catch (error) {
      setChatResponse("Error: Unable to fetch response.");
    }
  };

  return (
    <div className="app">
      <h1>AI Music Chatbot</h1>
      <ChatResponse response={chatResponse} />
      <ChatInput onSend={handleSend} />
    </div>
  );
}

export default App;
