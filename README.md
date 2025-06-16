# 🎙️ FurkanBot – AI-Powered Voice Assistant

Welcome to **FurkanBot** – an intelligent voice assistant built using **Flask**, **Google Gemini (Generative AI)**, and **gTTS**. It listens to your voice, processes your query using an AI model (with Furkan's persona), and responds both as text and speech.

Live demo coming soon!

---

## 🚀 Features

✅ Voice input via browser (Web Speech API)  
✅ Gemini-powered answers with personalized tone  
✅ gTTS voice output  
✅ Clean UI with loader  
✅ 5-second auto-record timeout  
✅ Easy to run locally

---

## 📦 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python + Flask
- **AI**: Google Generative AI (Gemini API)
- **Speech**: Web Speech API (input) + gTTS (output)

---

## 🧠 Project Structure

```text
FurkanBot/
├── app.py              # Flask backend
├── talker.py           # Gemini prompt logic (persona-based)
├── interview.txt       # Furkan's persona description
├── templates/
│   └── index.html      # Web interface (HTML + CSS + JS)
├── .env                # Stores API key (not committed)
├── requirements.txt    # Python dependencies
└── README.md
```
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/FurkanKhann/FurkanBot.git
cd FurkanBot
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 🧠 How It Works
Speech is captured using the browser’s microphone.
Text is sent to Flask backend (/ask endpoint).
Gemini generates a response based on interview.txt.
gTTS converts text to speech and returns it as base64 audio.
Audio + text is rendered in the browser.

### 🧪 Run the App
``` bash
python app.py
```
