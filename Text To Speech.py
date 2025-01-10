import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    phrases = [
        "Hello! I am Jarvis.",
        "How can I assist you?",
        "I am here to help with your tasks.",
        "Let me know what you need."
    ]

    # Speak each phrase continuously in a loop
    while True:
        for phrase in phrases:
            speak(phrase)
