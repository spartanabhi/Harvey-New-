import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning , Spartan abhi")
    elif hour>=12 and hour<16:
        speak("Good Afternoon , Spartan abhi")
    elif hour>=16 and hour<24:
        speak("Good evening , Spartan abhi")
    speak("Hello I'm Harvey Sir , Please tell me how may I help you")


def takeCommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('PLEASE! Say something')
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        data='something'
        data= r.recognize_google(audio,language='en-US')
        query = str(data)

    except sr.UnknownValueError:
        print ('Attention ! Google could not understand audio')
        data='Could not understand anything'
    except sr.RequestError as e:

       print ('Attention ! Could not request results from Google service.')

    print("User said : ",data)
    
def sendEmail(to , content) :
    server = smtp.SMTP("smtp.google.com" , 587)
    server.ehlo()
    server.starttls()
    server.login('yashveerai94@gmail.com', 'abhirai@1')
    server.sendmail('yashveerrai94@gmail.com',to,content)
    server.close()
    
    

    
    
if __name__ == "__main__":
    wishMe()
    takeCommand()
    
    while True :
        
        if 'Wikipedia' in query :
             speak("Searching wikipedia..")
             query = query.replace("Wikipedia","")
             results = wikipedia.summary(query ,  sentences= 3)
             speak("According to wikipedia ..")
             print(results)
             speak(results)
        elif 'open' in query :
             for i in range(1):
                 
                 a = query.split()
                 b = a[1]
                 webbrowser.open(b + '.com')
                 break
             break    
        elif 'play music' in query :
            for i in range(1):
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                #print(songs)
                r = random.randint(0,13)
                os.startfile(os.path.join(music_dir , songs[int(r)]))
                break
            break    
        elif "the time"  or 'time' or "The Time" in query:
            for i in range(1):
                Time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir , The Time is {Time}\n : ")
                print(Time)
                break
            break
        elif "email to" or 'Email To' in query:
            d = {Yash : "yashveerrai19@gmail.com" , Sethji:"chhawdiniranjan@gmail.com"}
            try:
                speak("What should I send Sir")
                content = takeCommand()
                speak("To whom should I send this Sir")
                for i in range(1):
                    too = takeCommand()
                    if d[i][key] in query:
                        to = d[i][value]
                        break
                break
                sendEmail(to,content)
                speak("Email has been sent!!")
            except exception as e:
                print(e)
                speak("Sorry  sir I'm unable to send this email")
                
                    
                