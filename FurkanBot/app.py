from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from talker import talker
from gtts import gTTS
import tempfile
import base64
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')  # serve frontend

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message', '')

    if not user_message:
        return jsonify({"error": "No message received"}), 400

    response_text = talker(user_message)

    tts = gTTS(response_text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        f.seek(0)
        audio_base64 = base64.b64encode(f.read()).decode()

    return jsonify({
        "reply": response_text,
        "audio_base64": audio_base64
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
