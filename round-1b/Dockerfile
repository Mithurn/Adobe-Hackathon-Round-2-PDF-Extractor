# Use Python 3.11 base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Create directories for input and output
RUN mkdir -p /app/input /app/output

# Set environment variables
ENV PYTHONPATH=/app/src

# Default command to run the application
CMD ["python", "src/docker_main.py"]

