# PDF Summary AI

A FastAPI-based web application that generates AI-powered summaries of PDF documents using OpenAI's GPT models. Built with clean architecture, dependency injection, and containerized deployment.

## 🚀 Features

- **PDF Upload & Processing**: Handle PDFs up to 50MB with text and table extraction
- **AI Summarization**: Generate comprehensive summaries using OpenAI GPT models
- **Clean Architecture**: Dependency injection with proper separation of concerns
- **RESTful API**: Well-structured endpoints with comprehensive documentation
- **Docker Ready**: Containerized deployment with Docker Compose
- **Configuration Management**: Environment-based configuration with validation

## 🛠️ Technology Stack

- **Backend**: FastAPI with Python 3.12
- **AI Integration**: OpenAI GPT API
- **PDF Processing**: pdfplumber for text and table extraction
- **Dependency Management**: Poetry
- **Dependency Injection**: dependency-injector
- **Containerization**: Docker & Docker Compose
- **Production Server**: Gunicorn with Uvicorn workers

## 📋 Prerequisites

- Python 3.12+
- Poetry
- Docker & Docker Compose (for containerized deployment)
- OpenAI API key

## ⚡ Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/Maks-Siglov/PDF-Summary-AI-.git
cd PDF-Summary-AI-
```

### 2. Environment Configuration
Edit .env file and configure your settings
```bash
# Copy the environment template
cp .env.template .env
```

### 3. Choose Your Setup Method

Option A: Local Development with Poetry
```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell

# Run the application
poetry run make run
```

Option B: Docker Compose
```bash
# Navigate to compose directory
cd docker/compose/

# Start the service
docker-compose up --build -d

# View logs
docker-compose logs -f
```

Option C: Docker
```bash
docker build --file docker/dockerfiles/pdf_summary_ai.Dockerfile -t pdf-summary-ai . && \
docker run -p 8080:8080 pdf-summary-ai
```

### 4. Access the Application
Interactive Docs: http://localhost:8080/docs
ReDoc Documentation: http://localhost:8080/redoc

## Configuration
The application uses environment variables for configuration. Copy .env.template to .env and configure the following settings:

```bash
PDF_SUMMARY_AI__SERVICE_SETTINGS__MODE=DEV
```
Purpose: Sets the application mode, there is no Interactive Docs in PROD mode
Values: DEV (development) / PROD (production)


```bash
PDF_SUMMARY_AI__PDF_SETTINGS__SIZE_MB_LIMIT=50
```
Purpose: Maximum allowed PDF file size in megabytes
Values: Integer


```bash
PDF_SUMMARY_AI__OPENAI_SETTINGS__MODEL="gpt-3.5-turbo"
```
Purpose: OpenAI model to use for summary generation
Values: "gpt-3.5-turbo" (fast, cost-effective) / "gpt-4" (higher quality)


```bash
PDF_SUMMARY_AI__OPENAI_SETTINGS__API_KEY=sk-proj-your-key-here
```
Purpose: Your OpenAI API key for authentication
Values: Your API key from https://platform.openai.com/api-keys


```bash
PDF_SUMMARY_AI__OPENAI_SETTINGS__TEMPERATURE=0.2
```
Purpose: Controls randomness in AI responses
Values: 0.0 (deterministic) to 2.0 (very creative)
