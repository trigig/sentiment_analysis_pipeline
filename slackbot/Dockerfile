#start with python image
FROM python:3.7-slim

#Set working directory inside the container
WORKDIR /app

#copyfile from source in the folder to the app directory in container
COPY . /app

#install packages in the requirement file
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python","chatbot.py"]
