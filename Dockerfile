# Set ubuntu
FROM ubuntu:latest

MAINTAINER Bruno Kanazawa

# Update
RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

EXPOSE 5000
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt


# Run app.py when the container launches
CMD ["python3.6", "app.py"]