# Aditi Voice Assistant

A Python-based voice assistant powered by Google's Gemini AI model that can perform various tasks through voice commands.

## Features

- Voice interaction using speech recognition
- Text-to-speech responses
- Web browsing capabilities
- Time telling functionality
- Google search integration
- AI-powered conversations using Gemini

## Prerequisites

- Python 3.8 or higher
- A Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AddieBaraiya/chat-assistant.git
cd chat-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key:
   - Get an API key from Google AI Studio
   - Replace the `GEMINI_API_KEY` in `main.py` with your key

## Usage

Run the assistant:
```bash
python main.py
```

### Voice Commands

- "open youtube" - Opens YouTube in default browser
- "open google" - Opens Google
- "open wikipedia" - Opens Wikipedia
- "open stackoverflow" - Opens Stack Overflow
- "open github" - Opens GitHub
- "the time" - Tells current time
- "how are you" - Responds with a greeting
- "search google for [term]" - Performs a Google search
- "aditi quit" - Exits the program

For any other input, the assistant will engage in conversation using the Gemini AI model.

## Troubleshooting

If you encounter microphone issues:
1. Ensure your microphone is properly connected
2. Check system permissions for microphone access
3. Try running the program with administrator privileges

## Dependencies

- SpeechRecognition
- pyttsx3
- google-generativeai
- PyAudio

## License

MIT License
