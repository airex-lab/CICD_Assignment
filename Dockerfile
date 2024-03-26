FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Train the model during the Docker image build phase
RUN python train.py

# The command to run when the container starts (default command)
CMD ["python", "test.py"]
