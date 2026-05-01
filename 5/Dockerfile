FROM selenium/standalone-chrome:latest

USER root
WORKDIR /app

COPY parser.py .
COPY server.py .
COPY requirements.txt .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]