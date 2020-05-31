FROM arm32v6/alpine:3.12

WORKDIR /app

COPY app.py /app/
COPY requirements.txt /app/

RUN apk add -U vim linux-headers musl-dev gcc git python3 python3-dev py3-pip
RUN pip install --no-cache --upgrade pip setuptools wheel
RUN pip install Adafruit_DHT --install-option="--force-pi2"
RUN pip install -r requirements.txt

CMD python3 /app/app.py
