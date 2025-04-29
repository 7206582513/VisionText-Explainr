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
git clone https://github.com/7206582513/VisionText-Explainr.git
cd VisionText-Explainr
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate it:

bash
Copy
Edit
venv\Scripts\activate   # Windows
or

bash
Copy
Edit
source venv/bin/activate   # macOS/Linux
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Install Tesseract
Download Tesseract for Windows: https://github.com/UB-Mannheim/tesseract/wiki

Make sure to set the tesseract_cmd path inside app.py:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
🚀 Run the App
bash
Copy
Edit
python app.py
Visit in your browser:

📍 http://127.0.0.1:5000/

🔐 API Configuration
This app uses the Groq LLM API.

Replace your API key inside app.py:

python
Copy
Edit
GROQ_API_KEY = "your-api-key"
GROQ_MODEL = "llama3-70b-8192"
📦 Tech Stack
Python + Flask

OpenCV

pytesseract

Groq API

Bootstrap 5

📸 Screenshot
(Add your screenshot link here)

Example:

markdown
Copy
Edit
<img width="938" alt="VisionText-Explainr Screenshot" src="https://your-screenshot-link.png" />
📜 License
MIT License – free to use and modify.

yaml
Copy
Edit


