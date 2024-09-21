from flask import Flask, render_template, request, url_for
import pickle
import numpy as np

# Load the model
model = pickle.load(open('classifier1.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    Nitrogen = float(request.form.get('Nitrogen'))
    Potassium = float(request.form.get('Potassium'))
    Phosphorous = float(request.form.get('Phosphorous'))

    # Make prediction
    result = model.predict(np.array([[Nitrogen, Potassium, Phosphorous]]))[0]

    # Map prediction to fertilizer name and image
    if result == 0:
        result = 'TEN-TWENTY SIX-TWENTY SIX'
        result_image = 'images/ten_twenty_six.jpg'
    elif result == 1:
        result = 'Fourteen-Thirty Five-Fourteen'
        result_image = 'images/fourteen_thirty_five.jpg'
    elif result == 2:
        result = 'Seventeen-Seventeen-Seventeen'
        result_image = 'images/seventeen_seventeen.jpg'
    elif result == 3:
        result = 'TWENTY-TWENTY'
        result_image = 'images/twenty_twenty.jpg'
    elif result == 4:
        result = 'TWENTY EIGHT-TWENTY EIGHT'
        result_image = 'images/twenty_eight_twenty_eight.jpg'
    elif result == 5:
        result = 'DAP'
        result_image = 'images/dap.jpg'
    else:
        result = 'UREA'
        result_image = 'images/urea.jpg'

    # Pass the correct image path to the HTML template
    return render_template('index.html', result=result, result_image=result_image)

if __name__ == "__main__":
    app.run(debug=True)
