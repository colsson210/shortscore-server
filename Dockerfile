# Use an official Python runtime as a parent image
FROM python:2.7.14

# Set the working directory to /app
WORKDIR /app

ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install -U flask-cors

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
