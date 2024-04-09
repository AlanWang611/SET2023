FROM python:3.9-slim


RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]