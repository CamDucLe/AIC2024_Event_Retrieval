# Use an official Python runtime as a base image
FROM python:3.11-bookworm

# Set timeout to 60 minutes before installing dependencies
RUN pip install --default-timeout=3600 future

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy files ... to ... 
COPY . .

# Clean up apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Command to ...
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8080"]
