# Fertilizer Recommendation System

This project is a **Fertilizer Recommendation System** that helps farmers determine the best fertilizer to use based on input features like soil type, crop, and nutrient deficiencies. It is implemented using Flask for the backend, with an integrated machine learning model to provide recommendations.


### 1. **Static Files**
- The `static/images` folder contains the images used to display different types of fertilizers, such as DAP, Urea, and others.

### 2. **Templates**
- The `templates/` directory holds the `index.html` file which serves as the main interface for the user to interact with the recommendation system.

### 3. **app.py**
- This is the Flask backend that powers the system. It handles user requests, interacts with the machine learning model (`classifier1.pkl`), and returns the fertilizer recommendation to the user.

### 4. **classifier1.pkl**
- A pre-trained machine learning model serialized in a `.pkl` file. This model classifies the input data and provides the fertilizer recommendation based on the training it has undergone.

### 5. **requirements.txt**
- This file contains the list of dependencies required to run the project. It can be installed using the following command:
  pip install -r requirements.txt


### Installation and Setup
- To run this project locally, follow the steps below:

### Clone the repository
-git clone <repository-url>
cd Fertilizer-Recommendation-System
* Install dependencies: Make sure you have Python installed, then run:
pip install -r requirements.txt
Run the Flask app:
python app.py
Open in Browser: The application will be running on http://127.0.0.1:5000. Open this link in your web browser.

### Usage
Open the web application in your browser.
Enter the required inputs (like soil type, crop type, and nutrient deficiencies).
Click the submit button, and the system will recommend the best fertilizer for your input conditions.

