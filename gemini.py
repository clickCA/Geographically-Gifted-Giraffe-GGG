import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv
import os
import google.generativeai as genai
from bs4 import BeautifulSoup
from markdown import markdown

def generate_gemini_content(place):
  # Load the environment variables from the .env file
  load_dotenv()

  # Fetch the GOOGLE_API_KEY environment variable
  GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

  genai.configure(api_key=GOOGLE_API_KEY)

  for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
      print(m.name)

  model = genai.GenerativeModel('gemini-pro')

  content = f"Travelers often lack engaging and accessible resources to learn about destinations. Traditional guidebooks are static and bulky, while online resources can be overwhelming. GGG aims to bridge this gap by offering a fun and interactive way to explore the world through a friendly chatbot.Entertainment Value:GGG's Quirky Personality: Infuse GGG's responses with humor, trivia, and unexpected facts to make learning about travel enjoyable.Can u explain {place} lore"
  response = model.generate_content(content)
  return response.text

def convert_md_to_text(text):
  html = markdown(text)
  fommated_string = "".join(
      BeautifulSoup(html, features="html.parser").findAll(string=True)
  )
  return (fommated_string)
  
if __name__ == "__main__":
  place = "Victory Monument in Bangkok, Thailand"
  result = generate_gemini_content(place)
  print(result)
