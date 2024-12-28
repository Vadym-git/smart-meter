from Reader_SFH_300 import ReaderSFH300  # Import the class for reading sensor data
from machine import ADC  # Import ADC module for analog-to-digital conversion (not used here but likely relevant to hardware setup)
from machine import Pin  # Import Pin module to handle GPIO pins (not used here but relevant to hardware setup)
from time import sleep  # Import sleep function for delays (not used in this asyncio implementation)
from wi_fi_connector import WiFiClient  # Import custom WiFi client class to manage WiFi connectivity
from MQTT_Client import MQTT_Client  # Import custom MQTT client class to handle MQTT communication
import uasyncio as asyncio  # Import MicroPython's asyncio library for asynchronous programming

# Define the main asynchronous function
async def run():
    # Initialize the ReaderSFH300 on GPIO pin 33 (sensor for reading data)
    reader = ReaderSFH300(33)
    
    # Initialize and connect to WiFi using SSID and password
    wifi = WiFiClient('wynsum_2G', 'LanAVadyM10012015')
    wifi.connect()

    # Initialize and connect to the MQTT broker with IP, port, and optional credentials
    mqtt = MQTT_Client('192.168.50.77', 1883, None, None)
    mqtt.connect()
    
    # Infinite loop to continuously send data
    while True:
        # Read data from the sensor (energy consumption in watt-hours)
        data = reader.get_counter()
        
        # Clear the sensor counter after reading the data
        reader.clear_counter()
        
        # Create a dictionary to represent the current consumption
        current_consumption = {"current_consumption": data}
        
        # Send the data to the specified MQTT topic
        mqtt.send_topic("gen_electricity_meter/Wh", current_consumption)
        
        # Wait for 60 seconds before the next iteration
        await asyncio.sleep(60)

# Start the asynchronous run function
asyncio.run(run())
