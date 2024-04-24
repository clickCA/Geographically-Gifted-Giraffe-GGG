import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Fetch the GOOGLE_API_KEY environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)




model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")


print(response.text)