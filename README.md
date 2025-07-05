# AI Photo Enhancer

This project is an AI-powered tool to restore and enhance photos.

## Project Structure

- `frontend/`: Contains the React + Vite frontend application.
- `backend/`: Contains the Python (Flask) backend API that handles image processing with AI models.

## Getting Started

### Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # on Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python app.py
   ```
   The backend will be running at `http://127.0.0.1:5001`.

### Frontend

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   The frontend will be running at `http://localhost:5173` (or another port if 5173 is busy).
