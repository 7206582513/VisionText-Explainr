from flask import Flask, render_template, request, send_file
import pytesseract
import cv2
import os
import io
import requests
import numpy as np
from pdf2image import convert_from_bytes
from werkzeug.utils import secure_filename

# --- Flask Setup ---
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- API Setup ---
GROQ_API_KEY = "Your_Groq_API_KEY"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

# --- Tesseract Path ---
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- OCR Text Extract ---
def extract_text(file_path):
    ext = file_path.split('.')[-1].lower()
    if ext in ['png', 'jpg', 'jpeg']:
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
    elif ext == 'pdf':
        with open(file_path, 'rb') as f:
            images = convert_from_bytes(f.read())
        text = ''
        for page in images:
            page_array = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)
            text += pytesseract.image_to_string(page_array)
    else:
        text = "Unsupported file format."
    return text

# --- Explain Text using Groq ---
def explain_text(text):
    if not text.strip():
        return "No text detected to explain."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": f"Explain this text simply: {text}"}
        ],
        "temperature": 0.5
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.text}"

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    detected_text = ''
    explained_text = ''

    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            detected_text = extract_text(filepath)
            explained_text = explain_text(detected_text)

    return render_template('index.html', detected_text=detected_text, explained_text=explained_text)

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True)
