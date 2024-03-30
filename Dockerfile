# Set the official python image as the base image
FROM python:3.11

# Set the working directory
WORKDIR /mlapp

# Copy the contents from the repo to the mlapp folder
COPY . /mlapp

# Install the required python packages
RUN pip install --no-cache-dir -r requirements.txt

# Train the model in the build phase
RUN python train.py

# Test the model upon running the container
CMD ["python", "test.py"]
