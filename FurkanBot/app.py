from flask import Flask, request, jsonify
from gtts import gTTS
import tempfile
import base64
from talker import talker  # This should be in talker.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access this API

# Optional route to test if server is alive
@app.route('/')
def home():
    return "✅ Voice bot is running..."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"error": "No message received"}), 400

    # Get response from Gemini via talker
    
    response_text = talker(user_message)
    print(response_text)

    # Convert to speech using gTTS
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
    app.run(host='0.0.0.0', port=5000)

