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
        audio_text = r.listen(source, timeout=5)  # Set a timeout for listening
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

def generate_response(user_input, database='tasks.db'):
    create_db()  # Ensure the database is created
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    greetings = ["hi", "hello"]
    response = "How can I help?"

    if "add task" in user_input:
        # Extract the task after "add task"
        task = user_input.split("add task", 1)[-1].strip()
        if task:
            cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            conn.commit()
            response = "Task added, anything else?"
        else:
            response = "Please specify the task to add."
    speak(response)
    conn.close()
    return response

def main():
    user_input = get_input()
    if user_input:
        response = generate_response(user_input)
        print(response)

    # Connect to the database
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Example: Fetch all tasks
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    for task in tasks:
        print(task)

    conn.close()

if __name__ == "__main__":
    main()
