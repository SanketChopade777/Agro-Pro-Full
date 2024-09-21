import os
import json
import google.generativeai as genai
from googletrans import Translator

# Get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Load the config file
config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

# Load the API key from config
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configure google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the translator
translator = Translator()


# Function to list available models and their capabilities
def list_available_models():
    models = genai.list_models()
    for model in models:
        print(f"Model ID: {model.name}, Capabilities: {model.capabilities}")


# Function to translate text
def translate_text(text, dest_language='en'):
    translated = translator.translate(text, dest=dest_language)
    return translated.text


# Function to load a specific Gemini model for the chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")  # Update model ID if necessary
    return gemini_pro_model


# Function for chatbot response with language translation
def gemini_pro_response(user_prompt, language='en'):
    gemini_pro_model = genai.GenerativeModel("gemini-pro")  # Update model ID if necessary

    # Translate the user prompt to English if it's not already in English
    if language != 'en':
        user_prompt = translate_text(user_prompt, dest_language='en')

    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text

    # Translate the response back to the user’s language
    if language != 'en':
        result = translate_text(result, dest_language=language)

    return result


# List available models and their capabilities
if __name__ == "__main__":
    list_available_models()
