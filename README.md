# AI Photo Enhancer

This application uses AI to enhance and upscale photos using Real-ESRGAN technology.

## Project Structure

- **Frontend**: React application hosted on Netlify
- **Backend**: Flask API hosted on Render.com

## Deployment Instructions

### Frontend Deployment (Netlify)

1. The frontend is already deployed at: https://ai-photo-enhancer.netlify.app

2. To update the frontend:
   ```
   cd frontend
   npm install
   npm run build
   ```
   Then deploy using Netlify CLI or GitHub integration.

### Backend Deployment (Render.com)

1. Sign up for a Render.com account if you don't have one.

2. Connect your GitHub repository to Render.

3. Create a new Web Service and select your repository.

4. Use the following settings:
   - **Name**: ai-photo-enhancer-backend
   - **Environment**: Python
   - **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Root Directory**: `backend`

5. Add the following environment variables:
   - `PYTHON_VERSION`: 3.10.13
   - `PORT`: 10000

6. Deploy the service.

## Local Development

### Frontend
```
cd frontend
npm install
npm run dev
```

### Backend
```
cd backend
pip install -r requirements.txt
python app.py
```

## API Endpoints

- `POST /enhance`: Enhances an uploaded image
- `GET /`: Health check endpoint

## Technologies Used

- **Frontend**: React, Vite, React Compare Slider
- **Backend**: Flask, Real-ESRGAN, OpenCV
- **Deployment**: Netlify (Frontend), Render.com (Backend)
