import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import openai
import datetime
import random

from config import apikey

chatStr = ""

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Utkarsha: {query}\n Jarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        print(f"Error in chat function: {e}")
        return "Some Error Occurred. Sorry from Jarvis"

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print(f"Error in ai function: {e}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source, timeout=5)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error occurred during speech recognition: {e}")
    return ""

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Hello Jarvis A.I")
    while True:
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours {min} minutes")
        elif "open facetime".lower() in query.lower():
            os.system("open /System/Applications/FaceTime.app")
        elif "open pass".lower() in query.lower():
            os.system("open /Applications/Passky.app")
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Jarvis Quit".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)

