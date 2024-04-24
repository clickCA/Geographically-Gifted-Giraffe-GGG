from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkintermd.frame import TkintermdFrame
from text_to_speech import text_to_speech
import pygame
pygame.init()

import requests
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

url = 'http://127.0.0.1:8000/find_place'
file_path = '/home/click/Desktop/Geographically-Gifted-Giraffe-GGG/test_img/test3.jpg'

headers = {
    'accept': 'application/json'
}

data = {}

response = requests.post(url, params={'file_path': filename}, headers=headers, data=data)

# Print the response
print(response.json())

place = response.json()['landmark']




response = requests.get(f'http://127.0.0.1:8000/gemini/{place}', headers=headers)
# Print the response
print(response.json())
text = response.json()['gemini_content']


path = text_to_speech(text)
my_sound = pygame.mixer.Sound(path)

my_sound.play()
