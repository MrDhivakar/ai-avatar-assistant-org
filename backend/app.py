from flask import Flask, request, jsonify
from ai_brain import reply
from emotion import detect_emotion
from database import save_chat
import os

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    text = request.json["message"]
    emotion = detect_emotion()
    ai = reply(text + " (user emotion: " + emotion + ")")
    save_chat(text, ai)
    return jsonify({"reply": ai, "emotion": emotion})

@app.route("/")
def home():
    return "AI Avatar Backend Running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)