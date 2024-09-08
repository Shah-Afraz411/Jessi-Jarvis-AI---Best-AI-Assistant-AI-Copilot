import speech_recognition as sr
import webbrowser
import pyttsx3
import requests


import musicLibrary
import google.generativeai as genai


genai.configure(api_key="AIzaSyCMNwO-7FgxvUgVEwmxNQx-L6QNZ6__dK8") #Gemini chatBot Api key

# import pyaudio
# import pocketsphinx


recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

newsKey = "d30ae576fe9f4fb3923cce4c37cb97a5"

def speak(text):
    engine.say(text)
    engine.runAndWait()    # run and wait method, it processes the voice commands.
    return 0

def process_audio(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"): # Speak "play song name"
         print(1)
         song = c.lower().split(" ")[1]   # Split the String into list by space and [1] position in string you want to select
         print("playing", song)
         if song in musicLibrary.music:

             webbrowser.open(musicLibrary.music[song])

    elif "news" in c.lower():

        if "tesla" in c.lower():
            response =  requests.get(
    "https://newsapi.org/v2/everything?q=tesla&from=2024-08-01&sortBy=publishedAt&apiKey="+newsKey)
            if response.status_code == 200:
                # Parsing the response to JSON format
                data = response.json()

                # Checking if the response contains articles
                if 'articles' in data:
                    articles = data['articles']

                    # Looping through each article and printing the title and description
                    for i, article in enumerate(articles, start=1):
                        print(f"Article {i}:")
                        print(f"Title: {article['title']}")
                        print(f"Description: {article['description']}\n")
                        speak(article['title'])
                else:
                    print("No articles found in the response.")
            else:
                print(f"Error fetching data: {response.status_code} - {response.reason}")
        elif "apple" in c.lower():
            response =  requests.get(
    "https://newsapi.org/v2/everything?q=apple&from=2024-08-31&to=2024-08-31&sortBy=popularity&apiKey="+newsKey)
            if response.status_code == 200:
                # Parsing the response to JSON format
                data = response.json()

                # Checking if the response contains articles
                if 'articles' in data:
                    articles = data['articles']

                    # Looping through each article and printing the title and description
                    for i, article in enumerate(articles, start=1):
                        print(f"Article {i}:")
                        print(f"Title: {article['title']}")
                        print(f"Description: {article['description']}\n")
                        speak(article['title'])
                else:
                    print("No articles found in the response.")
            else:
                print(f"Error fetching data: {response.status_code} - {response.reason}")
    else:


        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": "Hello"},
                {"role": "model", "parts": "Great to meet you. What would you like to know?"},
            ]
        )
        response = chat.send_message(c)
        print(response.text)
        speak(response.text)



    return 0
# say method on the engine that passing input text to be spoken
speak('initializing Jessi...')
while True:
    try:
        with sr.Microphone() as source:
            print("Listening!")

            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise


                # recognize speech using Sphinx
            try:
                audio = recognizer.listen(source, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)
                print(f"You said: {word}")
                if word.lower() in ["jassi", "jessi", "jessy", "jaisi"]  :
                    speak("Yes,Boss")
                    print("Jessy Active")
                    with sr.Microphone() as source:
                        print("What can I do for you Sir!")

                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio = recognizer.listen(source, phrase_time_limit=3)

                        try:
                            command = recognizer.recognize_google(audio)
                            process_audio(command)
                        except sr.UnknownValueError:
                            speak("Sorry Sir, I did not understand that.")

            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")

            except sr.RequestError:
                print("Could not request results from the speech recognition service.")
    except KeyboardInterrupt:
        print("Process interrupted by the user. Exiting...")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


