import speech_recognition as sr

r = sr.Recognizer()

def get_input():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

        try:
            # Recognize speech using Google
            user_input = r.recognize_google(audio_text)
            print("You said:", user_input)
            return user_input.lower()  # Lowercase for easier matching
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

def generate_response(user_input):
    greetings = ["hi", "hello"]
    if user_input in greetings:
        return "Hi, I am Mat!"
    else:
        return "How can I help?"

def main():
    user_input = get_input()
    if user_input:  # Only respond if we got valid input
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
