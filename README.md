## Resume Parser API

Django + LangChain + Groq

A production-ready REST API that uploads resumes (PDF files), extracts their content, and converts them into structured JSON using LangChain with Groq LLM.

Designed to be extensible for HR systems, ATS platforms, or AI-powered candidate screening tools.

## 🚀 Features

Upload resume files (PDF format)

Extract text using PyMuPDF

Parse resume content into structured JSON using LangChain + Groq

Validate structured output using Pydantic

Store parsed results in PostgreSQL (JSONField)

JWT Authentication support

CORS enabled

Filter and list resumes

API endpoints built with Django REST Framework

## 🧠 How It Works

User uploads a PDF resume.

PyMuPDF extracts raw text from the file.

The extracted text is sent to Groq LLM via LangChain.

The LLM converts unstructured resume text into structured JSON.

The JSON is validated using Pydantic schema.

The final structured result is stored in the database.

Pipeline:

PDF → Text Extraction → LLM Parsing → Schema Validation → Database Storage

## 🏗 Tech Stack

Backend:

Django

Django REST Framework

PostgreSQL

AI Layer:

LangChain (Core)

Groq API (LLM inference)

Pydantic (Structured schema validation)

Utilities:

PyMuPDF (fitz)

python-dotenv

requests

django-cors-headers

django-filter

djangorestframework-simplejwt

📂 Project Structure
resume_parser/
│
├── resumes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── parser.py
│   ├── urls.py
│
├── resume_parser/
│   ├── settings.py
│   ├── urls.py
│
├── .env
├── requirements.txt
└── manage.py
## ⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/resume-parser-api.git
cd resume-parser-api
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
## 🔑 Environment Variables

Create a .env file in the root directory:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/resume_db
GROQ_API_KEY=your_groq_api_key

Make sure python-dotenv is configured in settings.py.

## 🗄 Database Setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Run server:

python manage.py runserver
## 🔐 Authentication

This API uses JWT Authentication.

Obtain token:

POST /api/token/

Refresh token:

POST /api/token/refresh/

Add header to requests:

Authorization: Bearer <your_access_token>
## 📡 API Endpoints
Upload Resume
POST /api/resumes/

Body (form-data):

file: resume.pdf
Parse Resume
POST /api/resumes/<id>/parse/

## 🧪 Error Handling

Common errors:

400 → Invalid PDF or empty file

401 → Unauthorized (missing token)

405 → Wrong HTTP method (parse endpoint requires POST)

500 → LLM parsing failure

## 🧩 Future Improvements

Support DOCX files

Add asynchronous parsing (Celery)

Improve prompt engineering

Add skill scoring / ranking system

Add AI-based candidate matching

Add Swagger / OpenAPI documentation


## 👩‍💻 Author

Sa'er Hamzeh