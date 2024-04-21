from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
value = os.getenv("TEXT_TO_SPEECH_API_ENDPOINT")
print(value)
