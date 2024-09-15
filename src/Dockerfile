# Use a base Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy local files to the container
COPY . /app

RUN pip install -r requisites.txt

# Install Python dependencies
RUN pip install -e .[dev]

# Expose the application port
EXPOSE 5000

# Command to run the app
CMD ["python3", "run.py"]
