import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
<<<<<<< HEAD
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
=======
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")
genai.configure(api_key=api_key)
>>>>>>> 112230d (Initial commit)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
