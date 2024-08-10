FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]