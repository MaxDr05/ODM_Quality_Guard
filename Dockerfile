FROM python:3.10-slim
LABEL authors="calvin"

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y adb

RUN pip install -r requirements.txt

COPY . .

CMD ["python","main.py"]

