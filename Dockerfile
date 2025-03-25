# Use a lightweight Python base image
FROM python:3.9-slim

# Install Ghostscript for PDF compression
RUN apt-get update && apt-get install -y ghostscript && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script, requirements, and shell script into the container
COPY app.py .
COPY requirements.txt .
COPY run.sh .

# Install any Python dependencies
RUN pip install -r requirements.txt

# Entry point to the shell script
ENTRYPOINT ["bash", "run.sh"]
