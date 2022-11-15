FROM python:2.7.16

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y sqlite3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run.py"]
