

# Malicious URL Detection

A simple Flask web application for detecting whether a URL is malicious or not using a machine learning model.

## Project Structure

- `app.py`: Flask application script.
- `static/`: Folder for static files (e.g., CSS).
- `templates/`: Folder for HTML templates.
- `your_model_filename.pkl`: Trained machine learning model file.
- `your_vectorizer_filename.pkl`: TfidfVectorizer file.
- `data.csv`: Dataset file.
- `requirements.txt`: List of Python packages and versions.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/malicious-url-detection.git
   ```

2. Navigate to the project folder:

   ```bash
   cd malicious-url-detection
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

4. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Access the website locally at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Enter a URL in the provided input field.
2. Click the "Detect" button to check if the URL is malicious or not.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

