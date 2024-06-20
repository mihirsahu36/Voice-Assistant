import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=3)
            print('listening...')
            voice = listener.listen(source)
            if voice:
                command = listener.recognize_google(voice)
                command = command.lower()
                return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    return None

def run_assistant():
    try:
        command = take_command()
        if command:
            print(command)
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'day' in command:
                info = datetime.date.today().strftime('%A')
                print(info)
                talk(info)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'who is' in command:
                person = command.replace('who is ','')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'date' in command:
                talk(datetime.datetime.now().strftime('%Y-%m-%d'))
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            elif 'hello' in command:
                talk('hi')
            elif 'quit' in command:
                talk('Goodbye!')
                sys.exit()
            else:
                talk('Please say the command again.')
        else:
            talk('Please say the command again.')
    except KeyboardInterrupt:
        talk('Program terminated by user')
        sys.exit()
    except Exception as e:
        print(f"Error occurred: {e}")
        talk("Sorry, I didn't catch that. Could you please repeat your question?")

while True:
    run_assistant()
