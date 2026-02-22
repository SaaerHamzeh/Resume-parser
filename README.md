# Resume Parser API (Django + LangChain + Groq)

A Django REST API that uploads resumes (PDF) and parses them into structured JSON using LangChain + Groq LLM.

## Features
- Upload resume files (PDF)
- Extract text from PDF using PyMuPDF (fitz)
- Parse resume content into structured JSON via LangChain + Groq
- Store parsing results in the database (JSONField)
- Endpoints exposed via Django REST Framework

## Tech Stack
- Django + Django REST Framework
- LangChain (core)
- Groq (LLM API)
- PyMuPDF (PDF text extraction)
- python-dotenv (environment variables)
- Pydantic (data validation)
- requests (HTTP requests)
- django-cors-headers (CORS)
- django-filter (filtering)
- djangorestframework (API)
- djangorestframework-simplejwt (JWT authentication)
- PostgreSQL (database)

## Project Structure

