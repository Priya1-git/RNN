import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pt.init()  # don't use 'dummy'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            voice = listener.listen(mic)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if "kodi" in cmd:
                cmd = cmd.replace("kodi", "").strip()
                print(f"Command received: {cmd}")
    except Exception as e:
        print(f"Could not process audio: {e}")
    return cmd

def run():
    while True:
        cmd = hear()
        if cmd:
            print(f"Heard: {cmd}")
            if "play" in cmd:
                song = cmd.replace("play", "").strip()
                speak("Playing " + song)
                pk.playonyt(song)
            elif "stop" in cmd or "exit" in cmd:
                speak("Goodbye!")
                break
        else:
            print("No command detected. Listening again...")

# Start the assistant
run()
