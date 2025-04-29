# VisionText-Explainr
# VisionText Explainr 🧠🖼️

A Flask-based web application that extracts text from **images or PDFs** using Tesseract OCR and provides a **simple AI-powered explanation** using Groq LLM.

> 📌 Built with: Python, Flask, OpenCV, Tesseract OCR, Groq API, Bootstrap

---

## 💡 Features

- 📷 Upload **image** (`.jpg`, `.jpeg`, `.png`) or **PDF**
- 🔍 Extracts text using `pytesseract` and `OpenCV`
- 🤖 Explains the content in **simple language** using Groq AI
- 🌙 Clean **dark UI**, built with Bootstrap
- 📥 Download explained results

---

## 🔧 Installation

### 1. Clone the Repo

```bash
git clone [https://github.com/<your-username>/visiontext-explainr](https://github.com/7206582513/VisionText-Explainr).git
cd visiontext-explainr

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # macOS/Linux

### 3. Install Requirements
pip install -r requirements.txt

### 4. Install Tesseract
  Download Tesseract for Windows
Make sure to set the tesseract_cmd path in app.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

### 🚀 Run the App
python app.py
Then visit:
📍 http://127.0.0.1:5000/

### 🔐 API Configuration
This app uses the Groq LLM API.
Replace your API key in app.py:
GROQ_API_KEY = "your-api-key"
GROQ_MODEL = "llama3-70b-8192"

###📦 Tech Stack
Python + Flask

OpenCV

pytesseract

Groq API

Bootstrap 5

### 📸 Screenshots

<img width="938" alt="image" src="https://github.com/user-attachments/assets/8d0fcfc2-44c7-4750-b1e1-7f7173b4c484" />

### 📜 License
MIT License – free to use and modify.

