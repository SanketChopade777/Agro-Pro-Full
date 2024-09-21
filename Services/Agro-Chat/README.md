### AgroChat - Agriculture Chatbot
AgroChat is a chatbot designed to help farmers and agricultural professionals get recommendations for crops and fertilizers. It leverages machine learning models for intent classification and entity recognition, providing intelligent responses to users’ queries related to agriculture.

## Project Overview
AgroChat uses Google's Gemini AI models and integrates with a user-friendly web interface. It allows users to ask questions about crop recommendations, farming practices, and fertilizers and get responses based on their inputs.

## Features
Crop Recommendations: Suggests the best crops to grow based on various factors.
Fertilizer Suggestions: Recommends fertilizers depending on crop type and soil conditions.
Natural Language Processing: Interprets and responds to natural language queries.
Multilingual Support (Optional): The chatbot supports multiple languages (e.g., English, Marathi, Hindi, Tamil).
Web Integration: Can be deployed as a web application using Streamlit.

## Project Structure

├── .streamlit/          # Streamlit configuration files
│   └── config.toml      # Contains UI and server settings for Streamlit
├── config.json          # Configuration file with API keys and other settings
├── gemini_utility.py    # Utility functions for Gemini AI interaction
├── main.py              # Main application file (Streamlit app)
├── requirements.txt     # Python package dependencies



## Files and Directories
.streamlit/: Contains Streamlit configuration settings like theme, server options, etc.
config.json: Stores API keys and other necessary configuration details.
gemini_utility.py: Houses utility functions to load models, handle API interactions, and generate responses using the Gemini AI.
main.py: The primary application file that runs the chatbot interface via Streamlit.
requirements.txt: Lists all the Python dependencies needed for the project.


## Installation
Prerequisites
Python 3.x
An API key for Google Gemini AI (stored in config.json)
Steps to Run the Project

## Clone the repository:
git clone https://github.com/your-repo/agrochat.git
cd agrochat

## Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install the dependencies:
pip install -r requirements.txt
Add your API key:

Open the config.json file and insert your API key for Gemini AI.
# Run the chatbot using Streamlit:
streamlit run main.py
# Configuration
You will need to configure your API keys in config.json. Here's a sample:

{
  "gemini_api_key": "your-gemini-api-key"
}


## Usage
Once the chatbot is running, open the provided Streamlit link in your browser to interact with AgroChat. You can ask questions related to agriculture, crops, and fertilizers.