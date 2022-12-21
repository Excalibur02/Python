import datetime
import requests
import pywhatkit
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 120)
engine.say(" Hello ")
engine.say(" this is kashish at your service ")
engine.say("what can i do for you ")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


def kashish_cmd():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            # sr.adjust_for_ambient_noise(source, duration=0.2)
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)

            cmd = cmd.lower()
            if "kashish" in cmd:
                cmd = cmd.replace("kashish","")
                print(cmd)
    except :
        pass

    return cmd


def run_kashish():
    cmd = kashish_cmd()
    # print(cmd)
    if "play" in cmd:
        song = cmd.replace("play", "")
        talk("wait a bit i am playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in cmd:
        time = datetime.datetime.now().strftime("%H hours and %M minutes")
        talk("Current time is " + time)
    elif "weather" in cmd:
        city = "delhi"
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=29b56202195e471e213de207a4bb112f"
        json_data = requests.get(api).json()
        conditions = json_data['weather'][0]['main']
        temp = round((json_data['main']['temp'] - 273.15000), 5)
        talk(conditions + "would best describe the current weather condition in Delhi ")
        talk("the temperature feels somewhat around " + temp + "degree Celcius ")




    # elif "google" in cmd:
    #     import wikipedia as search
    #     data = cmd
    #     if "search" in cmd:
    #         data = cmd.replace("search", "")
    #     talk("This is what I found on google ")
    #     pywhatkit.search(data)
    #     talk(search.summary(data, 2))

#
# with open('speech.txt', mode='w') as file:
#     file.write(kashish_cmd())


run_kashish()
