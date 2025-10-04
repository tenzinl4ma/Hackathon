from flask import Flask, request, jsonify
import requests
import os
from flask import render_template

from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # set this in your env

@app.route("/nhan", methods = ['GET'])
def adsjflasldjf():
    return render_template("amongus.html")



@app.route("/groq", methods=["POST"])
def groq_proxy():
    if not GROQ_API_KEY:
        return jsonify({"error": "GROQ_API_KEY missing in environment"}), 500

    data = request.get_json()
    if data is None:
        return jsonify({"error": "Request must be valid JSON"}), 400

    try:
        resp = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",  # ← NO TRAILING SPACES
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": data.get("model", "llama-3.1-8b-instant"),
                "messages": data.get("messages", []),
                "max_tokens": data.get("max_tokens", 60),
                "temperature": data.get("temperature", 0.7)
            },
            timeout=10
        )
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        print("Groq error:", str(e))
        return jsonify({"error": "Failed to reach Groq API"}), 500
@app.route("/")
def home():
   return render_template("index.html")
  

@app.route("/ai-testing", methods=["GET"])
def ai_test():
    if not GROQ_API_KEY:
        return jsonify({"error": "GROQ_API_KEY is missing"}), 500

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model":"llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": "Say 'Flask-Groq test successful!' in 5 words."}],
                "max_tokens": 60,
                "temperature": 0.7
            },
            timeout=10
        )
        data = response.json()
        print("Groq full response:", data)  # 🔥 THIS IS CRITICAL

        if not response.ok:
            return jsonify({"status": "ERROR", "code": response.status_code, "body": data}), response.status_code

        choices = data.get("choices", [])
        if not choices:
            return jsonify({"status": "ERROR", "reason": "No choices in response", "raw": data}), 500

        reply = choices[0].get("message", {}).get("content", "").strip()
        if not reply:
            return jsonify({"status": "ERROR", "reason": "Empty content", "raw": data}), 500

        return jsonify({"status": "OK", "reply": reply})
    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5050,host='0.0.0.0')

