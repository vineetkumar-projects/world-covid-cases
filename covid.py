import requests
import json
from win32com.client import Dispatch

def voice(a,b):
    speak = Dispatch("SAPI.SpVoice")
    print("World:")
    print(f"    total comfirmed: {a}")
    print(f"    total death: {b}")
    speak.Speak(f"total comfirmed:{a}")
    speak.Speak(f"total death:{b}")
    


data = requests.get("https://api.covid19api.com/summary")
jsonData = data.text
pythonData = json.loads(jsonData)
world = pythonData["Global"]
total = world['TotalConfirmed']
death = world['TotalDeaths']
voice(total,death)
