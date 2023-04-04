import Weather as w
import pyttsx3 as p

if __name__ == '__main__':
    # I don't know what it is...
    engine = p.init()
    engine.setProperty('rate', 150)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    for loc in w.location:
        engine.say(f"The Temprature in {loc} is {w.dic['current']['temp_c']} and the Weather is {w.dic['current']['condition']['text']}")
        engine.runAndWait()

else:
    print("You don't have permission to run this program as Modules")