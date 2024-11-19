# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    imagemagick \
    libx11-6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY . .

# Expose a port if you plan to run a server (optional)
# EXPOSE 5000

# Define the command to run the script
CMD ["python", "your_script.py"]