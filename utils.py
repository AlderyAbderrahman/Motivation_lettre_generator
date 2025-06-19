import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_motivation_letter(inputs: dict) -> str:
    """
    Build the prompt and send it to Gemini.
    :param inputs: A dict with user inputs
    :return: Generated motivation letter (string)
    """

    prompt = f"""
You are a professional assistant for writing motivation letters.

Write a motivation letter for a student who is applying to:
→ Program: {inputs['program']}
→ University or Organization: {inputs['university']}

The student has the following background:
→ Field of study: {inputs['field']}
→ Experience: {inputs['experience']}

Career goals:

→ {inputs['goals']}

Preferred tone:
→ {inputs['tone']}

The letter should be well-structured, convincing, and no more than 400 words.
"""

    response = model.generate_content(prompt)
    return response.text.strip()
