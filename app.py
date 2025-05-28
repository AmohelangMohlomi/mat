import pyttsx3
import speech_recognition as sr
import sqlite3

# Initialize text-to-speech engine
def create_db():
    # connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


engine = pyttsx3.init()

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_input():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

        try:
            user_input = r.recognize_google(audio_text)
            print("You said:", user_input)
            return user_input.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
            return None
        except sr.RequestError:
            print("Could not connect to Google Speech Recognition service.")
            return None

def generate_response(user_input):
    greetings = ["hi", "hello"]
    if user_input in greetings:
        response = "Hi, I am Mat!"
    else:
        response = "How can I help?"
    speak(response)
    return response

def main():
    user_input = get_input()
    if user_input:
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
