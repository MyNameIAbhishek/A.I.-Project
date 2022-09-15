import pyttsx3
import datetime
import speech_recognition
import wikipedia
import webbrowser
import os
import smtplib

#I am here using the Speak API of Microsoft

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)

dict={"Ambur": "agarwalamber916@gmail.com"}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir")
    elif hour>=12  and hour<16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Jarvis. How may i help you Sir. You are too good Sir")

#  now this funtion takes the voice input by enabling MICROPHONE from the user and returns as a string output
def takes():
    r = speech_recognition.Recognizer()  # this recognizer class helps to recognize the voice
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # it takes 1 sec for me to take gap in between speaking of user
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Please Say that again.... ")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rocksabhishekRaghav313@gmail.com', 'Abhishek@1212')
    server.sendmail('rocksabhishekRaghav313@gmail.com', to, content)
    server.close()

if _name== "main_":

    wishme()
    while True:
        query = takes().lower()    # I convert this in lower case because every website has url in small letters

        # logic start here

        if 'wikipedia' in query:
            speak("Searching Wikipedia...Please wait")
            query = query.replace("wikipedia", "")
            result= wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            Mudir = 'D:\\songs'
            songs = os.listdir(Mudir)
            print(songs)
            os.startfile(os.path.join(Mudir, songs[0])) # i can use random module in this line

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"Sir the time is {strTime}")

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'email to ambur' in query:
            try:
                speak("What should i say?")
                content = takes()
                to ="agarwalamber916@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Raghav sir! I am unable to send this Email")