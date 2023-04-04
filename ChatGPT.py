import os
import openai
from time import sleep
import pyttsx3 as p

openai.api_key = "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"


while True:    
    question = input("Enter a question: \n")
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=1,
    max_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    Engine = p.init()
    voice = Engine.getProperty('voices')
    Engine.setProperty('voice', voice[1].id)
    Engine.setProperty('rate', 200)

    print(response['choices'][0]['text'])
    Engine.say(response['choices'][0]['text'])
    Engine.runAndWait()
