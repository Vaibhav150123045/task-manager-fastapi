# Use Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Default command
CMD ["uvicorn", "task_manager.main:app", "--host", "0.0.0.0", "--port", "8000"]