from gpiozero import MCP3008
import time

# Soil Moisture Sensor is connected to channel 0 of MCP3008
soil_moisture_sensor = MCP3008(channel=0)

while True:
    soil_moisture = soil_moisture_sensor.value
    print('Soil Moisture:', soil_moisture)
    time.sleep(1)
