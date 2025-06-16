import google.generativeai as genai


genai.configure(api_key="GEMINI_API_KEY")

# Load persona from file
with open("interview.txt", "r", encoding="utf-8") as file:
    persona_data = file.read()

def talker(user_prompt):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        prompt = f"""
You are Furkan Khan, answering as yourself.

Here is your background and personality:
{persona_data}

Now respond to this question as Furkan would: "{user_prompt}"

If the answer is not in the profile, respond thoughtfully in his tone (concise, practical, and honest).
"""
        response = model.generate_content(prompt)
        return response.text or "No response from Gemini."
    except Exception as e:
        print("❌ Gemini Error:", e)
        return "Gemini failed to generate content."
