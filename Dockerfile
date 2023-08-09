# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-dotenv

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

ENV DATABASE_URI=sqlite:///employees.sqlite3

# Start the Flask app when the container starts
CMD ["flask", "run", "--host", "0.0.0.0"]
