# Python Base Image
FROM python:3.11

# Creating working directory in the container
WORKDIR /cicd_assignment

# Copy the current directory contents into the container
COPY . /cicd_assignment

# Install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Train the model during building phase
RUN python train.py

# Executing the test.py when the container in run phase
CMD ["python", "test.py"]