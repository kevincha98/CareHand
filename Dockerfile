# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the Flask app port
EXPOSE 80

# Define the command to run the Flask app
CMD ["python", "Rcm.py"]
