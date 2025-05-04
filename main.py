import datetime
import random
import webbrowser
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import sys
import time
from config import GEMINI_API_KEY

# Configuration
genai.configure(api_key=GEMINI_API_KEY)

class VoiceAssistant:
    def __init__(self):
        # Initialize TTS engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        
        # Command mappings
        self.commands = {
            "open youtube": ("Opening YouTube", "https://www.youtube.com"),
            "open google": ("Opening Google", "https://www.google.com"),
            "open wikipedia": ("Opening Wikipedia", "https://www.wikipedia.com"),
            "open stackoverflow": ("Opening Stack Overflow", "https://www.stackoverflow.com"),
            "open github": ("Opening GitHub", "https://www.github.com"),
        }
        
        self.chat_history = []  # Add this line to store chat history

    def say(self, text):
        """Convert text to speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")
            # Reinitialize the engine if it fails
            try:
                self.engine = pyttsx3.init()
            except:
                print("Could not reinitialize TTS engine")

    def chat(self, query):
        """Process chat with Gemini AI"""
        try:
            model = genai.GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(query)
            reply = response.text.strip()
            # Store the conversation instead of printing
            self.chat_history.append({"user": query, "assistant": reply})
            self.say(reply)
            return reply
        except Exception as e:
            error_msg = f"Error in chat: {e}"
            self.chat_history.append({"user": query, "assistant": error_msg})
            self.say("Sorry, I couldn't process that.")
            return "Sorry, I couldn't process that."

    def display_chat_history(self):
        """Display the entire chat history"""
        print("\nChat History:")
        print("-" * 50)
        for entry in self.chat_history:
            print(f"You: {entry['user']}")
            print(f"Assistant: {entry['assistant']}")
            print("-" * 50)

    def take_command(self):
        """Listen for voice commands"""
        with sr.Microphone() as source:
            try:
                print("Listening...")
                # Reduce ambient noise and adjust for ambient sound
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Set timeout and phrase time limit
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                query = self.recognizer.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query.lower()
            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")
                return ""
            except sr.UnknownValueError:
                print("Could not understand audio")
                return ""
            except sr.RequestError:
                print("Could not request results from speech service")
                return ""
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit(0)
            except Exception as e:
                print(f"Error in speech recognition: {e}")
                return ""

    def process_command(self, query):
        """Process user commands"""
        if not query:  # Handle empty queries
            return True
            
        # Handle website opening commands
        for command, (message, url) in self.commands.items():
            if command in query:
                self.say(message)
                webbrowser.open(url)
                return True

        # Handle other specific commands
        if "the time" in query:
            current_time = datetime.datetime.now().strftime('%H:%M')
            self.say(f"The time is {current_time}")
        
        elif "how are you" in query:
            responses = ["I'm doing great!", "I'm fine, thank you.", "I'm good, how about you?"]
            self.say(random.choice(responses))
        
        elif "search google for" in query:
            search_term = query.replace("search google for", "").strip()
            self.say(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        
        elif "exit" in query or "quit" in query or "bye" in query:
            self.say("Goodbye!")
            return False
        
        else:
            print("Chatting...")
            self.chat(query)
        
        return True

    def run(self):
        """Main loop of the assistant"""
        print("Welcome to Aditi's chat assistant (Powered by Google Gemini)")
        self.say("Welcome to Aditi's chat assistant, powered by Google Gemini")
        
        try:
            running = True
            while running:
                query = self.take_command()
                running = self.process_command(query)
        except KeyboardInterrupt:
            print("\nGracefully shutting down...")
            self.say("Goodbye!")
        except Exception as e:
            print(f"Fatal error: {e}")
            self.say("An error occurred. Shutting down.")
        finally:
            if self.chat_history:  # Only display history if there were chat interactions
                self.display_chat_history()
            print("Thank you for using the assistant!")

if __name__ == '__main__':
    assistant = VoiceAssistant()
    assistant.run()
