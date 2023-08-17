from keras.models import load_model
from gtts import gTTS
import numpy as np
import random
import pickle
import json
import os
import speech_recognition as sr
import requests
import nltk
from nltk.stem import WordNetLemmatizer
from tkinter import *
import openai
from dotenv import load_dotenv

load_dotenv()
openai.organization = os.environ.get("OPENAI_ORG_ID")
openai.api_key = os.environ.get("OPENAI_API_KEY")
TOKEN = os.environ.get("TOKEN")


lemmatizer = WordNetLemmatizer()

model = load_model("chatbot_model.h5")
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

recognizer = sr.Recognizer()


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


def ask_openai(question):
    prompt = f"""{question}
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text.strip()


def ask_api(question):
    URL = f"https://pgpt.pactosolucoes.com.br/api/{TOKEN}/maxgpt?question={question}"
    response = requests.get(URL)
    txt = response.json().get("MaxGPT", "")
    texto_completo = " ".join(txt)
    return texto_completo


def send_to_api():
    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)

    if msg != "":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + "\n\n")
        ChatLog.config(foreground="#442265", font=("Verdana", 12))

        res = ask_api(msg)
        if not res:
            res = "Desculpe, não consegui obter uma resposta da API."

        ChatLog.insert(END, "Bot: " + res + "\n\n")

        base.update_idletasks()

        tts = gTTS(text=res, lang="pt-br")
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def send_to_openai():
    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)

    if msg != "":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + "\n\n")
        ChatLog.config(foreground="#442265", font=("Verdana", 12))

        res = ask_openai(msg)
        if not res:
            res = "Desculpe, não consegui obter uma resposta do ChatGPT."

        ChatLog.insert(END, "Bot: " + res + "\n\n")

        base.update_idletasks()

        tts = gTTS(text=res, lang="pt-br")
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def send():
    msg = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)

    if msg != "":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + "\n\n")
        ChatLog.config(foreground="#442265", font=("Verdana", 12))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + "\n\n")

        base.update_idletasks()

        tts = gTTS(text=res, lang="pt-br")
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def voice_input():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="pt-BR")
            EntryBox.delete("1.0", END)
            EntryBox.insert("1.0", text)
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
    except sr.UnknownValueError:
        print("Could not understand audio")


base = Tk()
base.title("ChatBot")
base.geometry("620x520")
base.resizable(width=False, height=False)

bg_color = "#f4f4f4"
btn_color = "#4b89ac"
btn_active_color = "#3b6978"
btn_text_color = "#ffffff"

base.configure(bg=bg_color)

ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial,12")
ChatLog.config(state=DISABLED, wrap="word")

scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog["yscrollcommand"] = scrollbar.set

button_width = 15
button_height = 2
button_spacing = 20

SendButton = Button(
    base,
    font=("Verdana", 10, "bold"),
    text="Send",
    width=button_width,
    height=button_height,
    bd=0,
    bg=btn_color,
    activebackground=btn_active_color,
    fg=btn_text_color,
    relief=FLAT,
    command=send,
)

VoiceButton = Button(
    base,
    font=("Verdana", 10, "bold"),
    text="Voice",
    width=button_width,
    height=button_height,
    bd=0,
    bg=btn_color,
    activebackground=btn_active_color,
    fg=btn_text_color,
    relief=FLAT,
    command=voice_input,
)

ApiButton = Button(
    base,
    font=("Verdana", 10, "bold"),
    text="Ask API",
    width=button_width,
    height=button_height,
    bd=0,
    bg=btn_color,
    activebackground=btn_active_color,
    fg=btn_text_color,
    relief=FLAT,
    command=send_to_api,
)

OpenAIButton = Button(
    base,
    font=("Verdana", 10, "bold"),
    text="Ask ChatGPT",
    width=button_width,
    height=button_height,
    bd=0,
    bg=btn_color,
    activebackground=btn_active_color,
    fg=btn_text_color,
    relief=FLAT,
    command=send_to_openai,
)

EntryBox = Text(base, bd=0, bg="white", width="50", height="5", font="Arial,12")

scrollbar.place(x=575, y=6, height=386)
ChatLog.place(x=10, y=6, height=386, width=560)
EntryBox.place(x=10, y=420, height=80, width=560)

OpenAIButton.place(x=10, y=360)
ApiButton.place(x=10 + (button_width * 1 * 8 + button_spacing), y=360)
VoiceButton.place(x=10 + (button_width * 2 * 8 + button_spacing * 2), y=360)
SendButton.place(x=10 + (button_width * 3 * 8 + button_spacing * 3), y=360)

base.mainloop()
