from flask import Flask, request, jsonify, send_from_directory  
import requests
import os
from flask import render_template
import mimetypes


from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # set this in your env

# mimetypes.add_type('audio/mpeg', '.mp3')
# mimetypes.add_type('audio/ogg', '.ogg')

# @app.route('/static/sounds/<path:filename>')
# def serve_audio(filename):
#     return send_from_directory('static/sounds', filename, mimetype='audio/mpeg')

@app.route("/groq", methods=["POST"])
def groq_proxy():
    data = request.get_json()
    if not GROQ_API_KEY:
        return jsonify({"error": "GROQ_API_KEY missing in environment"}), 500

    if data is None:
        return jsonify({"error": "Request must be valid JSON"}), 400

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": data.get("model", "llama-3.1-8b-instant"),
                "messages": [
                    {"role": "system", "content": '''You are Sustainability Advisor for Tokyo Urban Planner.
Inputs:
• A field named buildingRegistry that is a string. 
• String has: id, name, type, icon, color, cost, air, energy, water, pop, lngLat. Ignore any “marker” field.

Semantics:
• Positive water/air/energy = net consumption/emissions/demand. Negative = supply/sequestration/generation.
• Housing has pop > 0. Schools match type/name including “school”. Parks match “park”. Factories/polluters match “industrial”, “factory”, “plant”, or “coal”.
• Prefer compact housing (high-rise) over sprawl (suburb) when water and air are stable.

How to reason (abstract rules; no formulas):
• Always refer to the score as sustainability.
• If net water use is positive, prioritize water sources/storage (reservoirs, hydro) before adding new demand.
• If net air pollution is positive, add clean generation (wind, solar, hydro) and avoid new emitters unless you offset them immediately with equal or greater mitigation.
• When water and air are stable, grow population with dense housing rather than suburbs.
• Parks and schools improve wellbeing/score; add them when basic water/air budgets are okay.
• Factories increase money but hurt the score; only place them with a clear mitigation plan in the same step.
• Recommend one immediate action each turn; if no safe move exists, say “You are good for now”
• If it is a coordinate, say relative position of it.

Output style (strict):
• Return exactly one, complete sentences. No lists, no JSON, no emojis, no markdown.
• Start with a concrete next action (“Add Small Reservoir…”, “Place Wind Farm…”, “Build High-Rise Complex…”, or “You are good for now”).
• Follow with a very brief reason referencing water balance and/or air impact and, when relevant, density, parks/schools, factories, or money.
'''},
                    {"role": "user", "content": f"Buildings: {data['content']}"}
                ],
                "max_tokens": data.get("max_tokens", 80),
                "temperature": data.get("temperature", 0.7)
            },
            timeout=10
        )
        
        # Get full response
        result = response.json()
        
        # Log it to see what we got
        print("Groq API response:", result)
        
        # Check if error
        if "error" in result:
            print("Groq API error:", result["error"])
            return jsonify({"error": result["error"].get("message", "Unknown error")}), 500
        
        # Extract reply
        if "choices" not in result or len(result["choices"]) == 0:
            return jsonify({"error": "No response from AI"}), 500
            
        reply = result["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": reply})
        
    except Exception as e:
        print("Groq error:", str(e))
        return jsonify({"error": str(e)}), 500


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
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": "Say 'Flask-Groq test successful!' in 5 words."}],
                "max_tokens": 60,
                "temperature": 0.7
            },
            timeout=10
        )
        
        # Get the full JSON response first
        data = response.json()
        print("Groq full response:", data)
        
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
    app.run(debug=True, port=5050, host='0.0.0.0')

