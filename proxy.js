// proxy.js
import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

app.post("/groq", async (req, res) => {
  try {
    const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(req.body)
    });

    const data = await response.json();
    res.json(data);
  } catch (err) {
    console.error("Proxy error:", err);
    res.status(500).json({ error: "Proxy failed" });
  }
});

app.listen(5000, () => console.log("🛰️ Groq local proxy running on http://localhost:5000"));
