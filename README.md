# Order API Onboarding

This is a FastAPI application for order onboarding.

## Setup and Run Locally

1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080
   ```
5. **Access the API docs:**
   - Open [http://localhost:8080/docs](http://localhost:8080/docs) in your browser.

## Run with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t order-api-onboarding .
   ```
2. **Run the Docker container:**
   ```bash
   docker run -p 8080:8080 order-api-onboarding
   ```
3. **Access the API docs:**
   - Open [http://localhost:8080/docs](http://localhost:8080/docs) in your browser.

## Requirements
- Python 3.11+
- FastAPI
- Uvicorn

All dependencies are listed in `requirements.txt`. 