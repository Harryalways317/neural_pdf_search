FROM ubuntu:latest
LABEL authors="harishvadaparty"


# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV QDRANT_HOST=qdrant

# Run check_and_ingest.py when the container launches if data is not in Qdrant, then start FastAPI
CMD python init_collection.py

#&& uvicorn main:app --host 0.0.0.0 --port 8000
