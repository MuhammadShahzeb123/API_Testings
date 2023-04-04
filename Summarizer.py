import pyttsx3 as p
import ChatGPT as C
from time import sleep

if __name__ == '__main__':
    Engine = p.init()
    voice = Engine.getProperty('voices')
    Engine.setProperty('voice', voice[1].id)
    Engine.setProperty('rate', 200)

    C.question = input("Enter a question: \n")
    Engine.say(C.response['choices'][0]['text'])

    Engine.runAndWait()