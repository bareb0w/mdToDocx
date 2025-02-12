# Use official Python image
FROM python:3.10

# Install Pandoc
RUN apt-get update && apt-get install -y pandoc && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY main.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port (now 9000)
EXPOSE 9000

# Run the FastAPI app on port 9000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
