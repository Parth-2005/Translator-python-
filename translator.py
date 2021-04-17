import googletrans
import speech_recognition as sr
import pyttsx3
while True:
    translator = googletrans.Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query0001 = r.recognize_google(audio)
        detect = str(translator.detect(query0001).lang)
        print(detect)
        query001 = r.recognize_google(audio, language=detect)
        print(f"User said: {query001}\n")
        print(query001)
    except Exception as e:
        print(e)

    query = str(translator.translate(query001, dest='hi').text)
    print(query)
    pyttsx3.speak(query)