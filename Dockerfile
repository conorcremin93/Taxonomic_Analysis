# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install CA certificates and other system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates wget curl && rm -rf /var/lib/apt/lists/*

# Set trusted hosts to bypass SSL verification
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt

# Copy the Python script
COPY taxonomic_analysis.py ./

# Create output directory
RUN mkdir -p /app/output

# Default command
CMD ["python", "taxonomic_analysis.py"]
