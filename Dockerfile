# Base image with Python 3.11 environment
FROM python:3.11

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your training and testing code
COPY . .

# Train the model (build phase)
RUN python train.py

# Create a smaller image for running tests
# FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only test script and dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY test.py ./

# Execute test script when running the container
CMD [ "python", "test.py" ]
