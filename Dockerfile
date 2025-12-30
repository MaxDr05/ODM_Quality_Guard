FROM python:3.10-slim
LABEL authors="calvin"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","main.py"]

