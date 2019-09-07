# Humidity Temperature Sensor in Python for Raspberry PI

Most of the script is configurable using environment variables except the Certificate Bundle that is stored into the priv folder.

| Environment Variable | Description                                  | Example             |
|----------------------|----------------------------------------------|---------------------|
| MQTT_USER            | User used to Authenticate to MQTT Broker     | foo                 |
| MQTT_PASS            | Password used to Authenticate to MQTT Broker | bar                 |
| MQTT_BROKER_HOST     | MQTT Broker host                             | iot.eclipse.org     |
| MQTT_BROKER_PORT     | MQTT Broker port                             | 8883                |
| MQTT_CLIENT_ID       | Client identifier                            | kitchen-sensor      |
| TOPIC_TEMP           | Temperature MQTT Topic                       | kitchen/temperature |
| TOPIC_HUM            | Humidity MQTT Topic                          | kitchen/humidity    |
| TOPIC_ERRORS         | Errors MQTT Topic                            | kitchen/errors      |
| DHT_PIN              | PIN where DHT data PIN is connected to       | 4                   |
