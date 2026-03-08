
from flask import Flask, request, jsonify
from ai_brain import reply
from emotion import detect_emotion
from database import save_chat

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    text = request.json["message"]
    emotion = detect_emotion()
    ai = reply(text + " (user emotion: " + emotion + ")")
    save_chat(text, ai)
    return jsonify({"reply": ai, "emotion": emotion})

if __name__ == "__main__":
    app.run(port=5000)
