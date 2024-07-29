import speech_recognition as sr
import webbrowser # for opening browser and getting information
import pyttsx3 # for text to speech
import music_liberary


recognizer = sr.Recognizer() # here "Recognizer" is a class which recognizes the speech
engine = pyttsx3.init() # initializes the pyttsx3 module
newsapi = "07fa9db76cc34d7db032b787398adf33"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    speak("yes")
    if "open google" in c.lower(): # or c.lowre() == "open google"
        speak("opening google")
        webbrowser.open("https://google.com")
        
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
        
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
        
    elif "open instagram" in c.lower():
        speak("opening instagram")
        webbrowser.open("https://instagram.com")
        
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
        
    elif "song" in c.lower():
        song = c.lower().split()[1]
        link = music_liberary.english_music[song]
        webbrowser.open(link)
            
    elif "music" in c.lower():
        song = c.lower().split()[1]
        link = music_liberary.naruto_theme_songs[song]
        webbrowser.open(link)

    elif c.lower() == "listen":
        process_command(command)
    elif "you are my best friend" in c.lower():
        speak("yes, of course we are good friends after all i am your creation, master")
    elif "we are good friends" in c.lower():
        speak("yes, of course we are good friends after all i am your creation, master")

    # else:
    #     # let openAI handel this mess
    #     # but it cant happen bcs 

if __name__ == "__main__": 
    speak("Initializing Jaaarvis.....")
    
    while True:
        # listen for the wake word - "Jarvis"
        # obtain audio from microphone
        r = sr.Recognizer()
        print("recognizing..........")
        try:
            with sr.Microphone() as source:
                print("Listening........")
                audio = r.listen(source)
                command = r.recognize_google(audio)
            if command.lower() == "jarvis" or "hey jarvis":
                speak("Yes mster my orders")
                # listen for command
                with sr.Microphone() as source:
                    print("jarvis active.......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)
                    
            print("thanks")
            
        except Exception as e:
            print("Error;{0}".format(e))
    
