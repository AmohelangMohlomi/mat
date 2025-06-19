from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)







































# import pyttsx3
# import speech_recognition as sr
# import sqlite3
# from tabulate import tabulate



# Initialize text-to-speech engine
# def create_db():
#     # connect to SQLite database (or create it if it doesn't exist)
#     conn = sqlite3.connect('tasks.db')
#     mycursor = conn.cursor()
#     mycursor.execute("CREATE TABLE tasks(task,dealine)")
#     mycursor.execute("INSERT INTO tasks VALUES('Study for python test','friday')")

#     mycursor.execute("SELECT * FROM tasks")
#     rows = mycursor.fetchall()
    
#     mycursor.execute("PRAGMA table_info(tasks)")
#     cols = [cols[0] for column in mycursor.fetchall()]
#     print(tabulate(rows, headers=cols,tablefmt="grid"))
#     # conn.commit()
#     conn.close()
# create_db()

# engine = pyttsx3.init()

# r = sr.Recognizer()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def get_input():
#     with sr.Microphone() as source:
#         print("Talk")
#         audio_text = r.listen(source, timeout=5)  # Set a timeout for listening
#         print("Time over, thanks")

#         try:
#             user_input = r.recognize_google(audio_text)
#             print("You said:", user_input.split())
#             return user_input.lower()
#         except sr.UnknownValueError:
#             print("Sorry, I did not get that.")
#             return None
#         except sr.RequestError:
#             print("Could not connect to Google Speech Recognition service.")
#             return None

# def generate_response(user_input, database='tasks.db'):
#     create_db()  # Ensure the database is created
#     conn = sqlite3.connect(database)
#     cursor = conn.cursor()
#     greetings = ["hi", "hello"]
#     response = "How can I help?"

#     if "add task" in user_input:
#         # Extract the task after "add task"
#         task = user_input.split()
#         print(f"split input: {task} ")
#         if task:
#             # cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
#             conn.commit()
#             response = "Task added, anything else?"
#         else:
#             response = "Please specify the task to add."
#     speak(response)
#     conn.close()
#     return response

# def main():
#     user_input = get_input()
#     if user_input:
#         response = generate_response(user_input)
#         print(response)

#     # Connect to the database
#     conn = sqlite3.connect('tasks.db')
#     cursor = conn.cursor()

#     # Example: Fetch all tasks
#     cursor.execute("SELECT * FROM tasks")
#     tasks = cursor.fetchall()

#     for task in tasks:
#         print(task)

#     conn.close()

# # if __name__ == "__main__":
# #     main()
