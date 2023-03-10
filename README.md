# Humidity Temperature Sensor in Python for Raspberry PI

Most of the script is configurable using environment variables.

| Environment Variable | Description                                  | Example             |
|----------------------|----------------------------------------------|---------------------|
| MQTT_USER            | User used to Authenticate to MQTT Broker     | foo                 |
| MQTT_PASS            | Password used to Authenticate to MQTT Broker | bar                 |
| MQTT_BROKER_HOST     | MQTT Broker host                             | iot.eclipse.org     |
| MQTT_BROKER_PORT     | MQTT Broker port                             | 8883                |
| MQTT_TLS_ENABLE      | Enable TLS                                   | true                |
| MQTT_CLIENT_ID       | Client identifier                            | kitchen-sensor      |
| TOPIC_PREFIX         | MQTT Topic Prefix without last /             | kitchen             |
| DHT_PIN              | PIN where DHT data PIN is connected to       | 4                   |

### How to run
#### Clone Repo
`git clone https://github.com/scudelletti/humidity-temperature-sensor-python.git`

#### Enter project folder
`cd humidity-temperature-sensor-python`

#### Install libraries
`pip3 install -r requirements.txt`

#### After exporting the environment variables run:
`python3 app.py`

### Build Image
`docker buildx build . -t scudelletti/sensor-humidity-temperature:latest`
