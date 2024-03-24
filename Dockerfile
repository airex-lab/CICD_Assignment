###Intalling python
FROM python:3.11
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

# Copy the model training script into the container at /app
COPY train.py .

# Copy the data folder into the container at /app/data
COPY data ./data

# Train the model during the build phase
RUN python train.py

# Copy the test script into the container at /app
COPY test.py .

# Command to run the test script when the container starts
CMD ["python", "test.py"]
