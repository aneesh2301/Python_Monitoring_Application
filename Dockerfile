FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    build-essential \
    --no-install-recommends \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
# dependencies should be copied from local to container 
COPY requirements.txt . 

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]