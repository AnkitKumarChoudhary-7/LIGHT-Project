import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import datetime
import os
import subprocess
from openai import OpenAI
import pywhatkit


client = OpenAI(api_key="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")

def ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def say(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
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

def send_whatsapp_message():
    contacts = {
        "abhijeet":"+919692991957","snorlax":"+919692977283",
        "swayam":"+917750941501","mummy":"+917979844814"
    }
    say("whom do you want to send message sir..?")
    name = takeCommand()

    if name and name.lower() in contacts:
        number = contacts[name.lower()]
        say(f"What is the message for {name} , sir...?")
        message = takeCommand()

        if message:
            say(f"Sending message to {name}...")
            pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
            say("Message sent sir.")
    else:
        say("I couldn't find that contact in your list.")

def playMusic():
    music_path = r"C:\Users\ANKIT\Documents\Semparo.mp4"
    os.startfile(music_path)
    say("Playing music sir...")


# ------------------------- MAIN PROGRAM -------------------------

if __name__ == "__main__":
    say("Hello Sir, I am Light, your virtual assistant. Can I do something for you?")
    print("I am listening...")

    query = takeCommand()

    if query:
        query = query.lower()

        if "play music" in query:
            playMusic()

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The time is {time} Sir")

        elif "open vs code" in query:
            subprocess.Popen(r"C:\Users\ANKIT\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            say("Opening VS Code sir...")

        elif "open chrome" in query:
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            say("Opening Chrome sir...")

        elif "my idol" in query:
            say("Your idol is Cristiano Ronaldo sir...")

        elif "best player" in query:
            say("The best player in the world is Cristiano Ronaldo sir...")

        elif "anime character" in query:
            say("The best anime character is Son Goku Sir....")

        elif "send message" in query:
            send_whatsapp_message()

        elif "light" in query:
            prompt = query.replace("light", "").strip()
            answer = ai(prompt)
            say(answer)
            print(answer)

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
                    say(f"Opening {site[0]} sir...")
                    wb.open(site[1])
                    matched = True
                    break

            if not matched:
                say("Sorry sir, I didn't understand that command.")

    else:
        say("I'm sorry, I did not understand that.")