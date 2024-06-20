# Voice Assistant README

This Python script implements a simple voice assistant using various libraries for speech recognition, text-to-speech, web scraping, and fetching information from online sources.

## Modules Used:

### 1. `sys`
- **Purpose:** Provides access to system-specific parameters and functions.
- **Usage:** Used for exiting the program (`sys.exit()`) when the user chooses to quit.

### 2. `speech_recognition` (imported as `sr`)
- **Purpose:** Library for performing speech recognition.
- **Usage:** Listens to user commands via microphone (`sr.Microphone`), recognizes speech (`recognize_google`), and handles errors (`UnknownValueError`, `RequestError`).

### 3. `pyttsx3`
- **Purpose:** Text-to-speech conversion library.
- **Usage:** Converts text strings to spoken audio (`engine.say(text)` and `engine.runAndWait()`).

### 4. `pywhatkit`
- **Purpose:** Library for automation tasks on web platforms like YouTube.
- **Usage:** Plays requested songs on YouTube using `pywhatkit.playonyt(song)`.

### 5. `datetime`
- **Purpose:** Provides classes for manipulating dates and times.
- **Usage:** Retrieves and formats current date (`datetime.date.today().strftime('%A')`) and time (`datetime.datetime.now().strftime('%I:%M %p')`).

### 6. `wikipedia`
- **Purpose:** Library for accessing and parsing Wikipedia data.
- **Usage:** Retrieves summaries from Wikipedia based on user queries (`wikipedia.summary(person, 1)`).

### 7. `pyjokes`
- **Purpose:** Library for generating random jokes.
- **Usage:** Fetches a random joke (`pyjokes.get_joke()`).

## Functions:

### 1. `talk(text)`
- **Purpose:** Converts text to speech and speaks it out loud.
- **Parameters:** `text` (string) - The text to be spoken.
- **Usage:** Used to provide responses and information audibly to the user.

### 2. `take_command()`
- **Purpose:** Handles microphone input, performs speech recognition, and returns the recognized command.
- **Usage:** Listens for user commands, recognizes them using Google Speech Recognition, and converts the recognized text to lowercase for command processing.

### 3. `run_assistant()`
- **Purpose:** Main function to run the voice assistant.
- **Usage:** Calls `take_command()` to get user input, processes the command based on keywords (`play`, `day`, `time`, `who is`, `date`, `joke`, `hello`, `quit`), and uses `talk()` to respond audibly to the user.
- **Error Handling:** Catches exceptions, handles keyboard interrupts (`KeyboardInterrupt`), and provides feedback for unrecognized commands or errors.

## How to Use:

1. Ensure all necessary Python libraries (`speech_recognition`, `pyttsx3`, `pywhatkit`, `wikipedia`, `pyjokes`) are installed.
   
   ```bash
   pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes
