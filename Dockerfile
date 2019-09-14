FROM arm32v6/alpine:3.10

WORKDIR /app

COPY app.py /app/
COPY priv /app/priv
COPY requirements.txt /app/

RUN apk add -U vim linux-headers musl-dev gcc git python3 python3-dev
RUN pip3 install --no-cache --upgrade pip setuptools wheel
RUN pip3 install Adafruit_DHT --install-option="--force-pi2"
RUN pip3 install -r requirements.txt

CMD python3 /app/app.py
