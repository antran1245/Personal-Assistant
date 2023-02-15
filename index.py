import speech_recognition as sr

# Print all the available input devices
def printDevice():
    for i in range(0, len(sr.Microphone.list_microphone_names())):
        if "Microphone" in sr.Microphone.list_microphone_names()[i]:
            print(i, sr.Microphone.list_microphone_names()[i])

# Turn mic audio input into text
def micToText():
    with sr.Microphone(device_index=1) as source:
        print('Talk')
        audio_text = sr.Recognizer().listen(source)
        print("Time to talk is over.")

    recognize_text = ""
    try:
        recognize_text = sr.Recognizer().recognize_google(audio_text)
        print("Text: "+recognize_text)
    except:
        print("Could not recognize voice input")

    print("Final result " + recognize_text)


if __name__ == "__main__":
    # printDevice()
    micToText()
