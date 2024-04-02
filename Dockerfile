# Using Python3.9 as a base image
FROM python:3.9

# Setting working directory in the container
WORKDIR /app

# Copying the requirements file and installing dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copying the repository into the container
COPY . .

# Running the training script
RUN python train.py

#Running and testing script
CMD ["python", "test.py"]
