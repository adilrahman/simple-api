FROM python:3.10.4-slim

RUN apt-get update && apt-get install -y 

COPY . /app 

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]
