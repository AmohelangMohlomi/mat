import speech_recognition as sr

# Initializing recognizer class (for recognizing the speech)
r= sr.Recognizer()

# Reading Microphone source
# Listening to the speech and storing it in the audio_text variable.
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over,thanks")

    # recognize_() method will throw a request
    # error if the API is unreachable,
    # hence the exception handling

    try:
        # Using google speech recognition
        print("Text: "+ r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")    

