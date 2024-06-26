from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load("model_file.pkl")
vectorizer = joblib.load("vectorizer_file.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the URL from the request
    url = request.json['url']

    # Vectorize the input URL
    url_vector = vectorizer.transform([url])

    # Make a prediction
    prediction = model.predict(url_vector)

    # Return the result as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for detailed error messages