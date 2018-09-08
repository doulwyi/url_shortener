# Set ubuntu
FROM ubuntu:latest

# Update
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Run app.py when the container launches
CMD ["python", "app.py"]