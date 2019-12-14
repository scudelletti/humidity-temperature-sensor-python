import os
import time
import paho.mqtt.client as paho

# DHT imports
import Adafruit_DHT

# BME280 imports
import bme280
import smbus2

MQTT_USER = os.environ.get('MQTT_USER')
MQTT_PASS = os.environ.get('MQTT_PASS')
MQTT_BROKER_HOST = os.environ.get('MQTT_BROKER_HOST')
MQTT_BROKER_PORT = int(os.environ.get('MQTT_BROKER_PORT'))

MQTT_CLIENT_ID = os.environ.get('MQTT_CLIENT_ID')
TOPIC_PREFIX = os.environ.get('TOPIC_PREFIX')

DHT_PIN = int(os.environ.get('DHT_PIN'))
DHT_SENSOR = Adafruit_DHT.DHT22

MQTT_TLS_CERT_PATH = "priv/mqtt-broker-ca-bundle.crt"

TOPIC_DHT_TEMP = TOPIC_PREFIX + "/DHT22/temperature"
TOPIC_DHT_HUM = TOPIC_PREFIX + "/DHT22/humidity"
TOPIC_BME_TEMP = TOPIC_PREFIX + "/BME280/temperature"
TOPIC_BME_HUM = TOPIC_PREFIX + "/BME280/humidity"
TOPIC_BME_PRES = TOPIC_PREFIX + "/BME280/pressure"

I2C_PORT = 1
BME_ADDRESS = 0x76 # Other BME280s may be different use i2cdetect to see addresses
I2C_BUS = smbus2.SMBus(I2C_PORT)

bme280.load_calibration_params(I2C_BUS, BME_ADDRESS)

while True:
    # Connect to MQTT
    client = paho.Client(MQTT_CLIENT_ID)
    client.tls_set(MQTT_TLS_CERT_PATH)
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

    # DHT
    dht_humidity, dht_temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if dht_humidity is not None and dht_temperature is not None:
        client.publish(TOPIC_DHT_TEMP, dht_temperature)
        client.publish(TOPIC_DHT_HUM, dht_humidity)
    else:
        error = "ERROR CLIENT: %s" % MQTT_CLIENT_ID
        print(error)

    #BME280
    bme_data = bme280.sample(I2C_BUS, BME_ADDRESS)
    bme_humidity  = bme_data.humidity
    bme_temperature = bme_data.temperature
    bme_pressure  = bme_data.pressure

    if bme_humidity is not None and bme_temperature is not None and bme_pressure is not None:
        client.publish(TOPIC_BME_TEMP, bme_temperature)
        client.publish(TOPIC_BME_HUM, bme_humidity)
        client.publish(TOPIC_BME_PRES, bme_pressure)
    else:
        error = "ERROR CLIENT: %s" % MQTT_CLIENT_ID
        print(error)

    time.sleep(2)
