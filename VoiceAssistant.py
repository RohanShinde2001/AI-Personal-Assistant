import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import smtplib
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices [ 1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good morning!")
    elif hour>=12 and hour<16:
        speak("good afternoon")
    elif hour>=16 and hour<19:
        speak("good evening")
    else:
        speak("Hello sir")

    speak("I am Grace How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening your command!!!....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("can't recognize your voice say it again.....")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohanshinde96k@gmail.com', 'Shinde@123')
    server.sendmail('rohanshinde96k@gmail.com', to, content)
    server.close()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("Grace","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No output available")



if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

   #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            vid_dir = 'D:/video'
            video = os.listdir(vid_dir)
            print(video)
            os.startfile(os.path.join(vid_dir, video[0]))

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(os.path.join(chromePath))


        elif 'show my resume' in query:
            resumePath = "D:\RohanResume.pdf"
            os.startfile(os.path.join(resumePath))

        elif 'send mail to vishal' in query :
             try:
                 speak("what should i say")
                 content = takeCommand()
                 to = "vishalpawar774385@gmail.com"
                 sendemail(to, content)
                 speak("email has been sent!!!")
             except Exception as e:
                 print(e)
                 speak("sorry i am not able to send this mail!!!")


        else:


            speak('searching on google...')

            searchGoogle(query)

        break

