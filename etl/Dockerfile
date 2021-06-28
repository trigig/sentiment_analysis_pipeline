#Start with an official image as parent image
FROM python:3.7-slim

#Set working directory inside the container
WORKDIR /app

#Copy files from the source in your computer to the /app directory in the container
COPY . /app

#Install packages in the requirements file
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#What to run when container launches
CMD ["python", "etl.py"]