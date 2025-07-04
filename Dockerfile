# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed for opencv-python
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy only the requirements file to leverage Docker cache
COPY backend/requirements.txt .

# Install Python dependencies from requirements.txt, using a faster index for torch
RUN pip install --no-cache-dir -r requirements.txt --index-url https://download.pytorch.org/whl/cpu

# Copy the backend folder and the built frontend folder
COPY backend /app
COPY frontend/dist /app/frontend/dist

# Install basicsr and realesrgan from the cloned repos
RUN pip install /app/models/basicsr
RUN pip install /app/models/realesrgan

# Expose the port the app runs on
EXPOSE 8000

# Run the app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "4", "--timeout", "120", "app:app"]
