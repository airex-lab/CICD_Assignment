# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Train the model during the build
RUN python train.py

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME ASSIGNMENT3

# Run test.py when the container launches
CMD ["python", "test.py"]
