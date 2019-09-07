import Adafruit_DHT
import paho.mqtt.client as paho
import os
import time

MQTT_USER = os.environ.get('MQTT_USER')
MQTT_PASS = os.environ.get('MQTT_PASS')
MQTT_BROKER_HOST = os.environ.get('MQTT_BROKER_HOST')
MQTT_BROKER_PORT = int(os.environ.get('MQTT_BROKER_PORT'))

MQTT_CLIENT_ID = os.environ.get('MQTT_CLIENT_ID')
TOPIC_TEMP = os.environ.get('TOPIC_TEMP')
TOPIC_HUM = os.environ.get('TOPIC_HUM')
TOPIC_ERRORS = os.environ.get('TOPIC_ERRORS')

MQTT_TLS_CERT_PATH = "priv/mqtt-broker-ca-bundle.crt"

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = int(os.environ.get('DHT_PIN'))

client = paho.Client(MQTT_CLIENT_ID)
client.tls_set(MQTT_TLS_CERT_PATH)
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        client.publish(TOPIC_TEMP, temperature)
        client.publish(TOPIC_HUM, humidity)
    else:
        error = "ERROR CLIENT: %s" % MQTT_CLIENT_ID
        client.publish(TOPIC_ERRORS, error)

    time.sleep(2)
