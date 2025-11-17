import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import datetime
import os
import subprocess


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except:
        print("Sorry, I couldn't understand. Please say that again.")
        return None


def playMusic():
    music_path = r"C:\Users\ANKIT\Documents\Semparo.mp4"
    os.startfile(music_path)
    say(f"Playing music sir..... ")


if __name__ == "__main__":
    say("Hello Sir , I am Light , Your Virtual Assistant, Can I do something for you?")
    print("I am listening...")

    query = takeCommand()

    # Ensure query exists before using .lower()
    if query:
        query = query.lower()

        if "play music" in query:
            playMusic()

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The time is {time} Sir")

        elif "open vs code" in query:
            subprocess.Popen(r"C:\Users\ANKIT\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            say(f"Opening vs code sir....")

        elif "open chrome" in query:
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            say(f"Opening chrome sir....")


        else:
            sites = [
                ["youtube", "https://www.youtube.com"],
                ["wikipedia", "http://www.wikipedia.com"],
                ["google", "http://www.google.com"],
                ["instagram", "https://www.instagram.com"]
            ]

            matched = False

            for site in sites:
                if site[0] in query:
                    say(f"Opening {site[0]} , Sir...")
                    matched = True
                    wb.open(site[1])
                    break

            if not matched:
                say("Sorry sir, I didn't understand that command.")

    else:
        say("I'm sorry, I did not understand that.")
