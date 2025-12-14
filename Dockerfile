FROM python:3.12-slim

# Set the root workdir for your project
WORKDIR /app

RUN apt-get update && apt-get install -y docker.io

# Copy only backend requirements first for caching
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the rest of the project
COPY . .

# Run uvicorn pointing to backend.app.main
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
