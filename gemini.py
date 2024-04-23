import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

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