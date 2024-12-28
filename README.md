# **Modular Data Acquisition and Transmission System**

## **Overview**

This project is a flexible, modular system designed to read data from various sensors, process it, and transmit the data over different communication protocols. Built entirely from scratch, the system showcases a combination of software development, modern IT technologies, and practical knowledge of physics and electronics.

The architecture is modular, allowing for easy extension of functionality. Whether you need to work with a new type of sensor, switch to a different communication method, or use an alternate data transmission protocol, the system can adapt with minimal changes.

## **Features**

* **Data Source Module**: Supports multiple sensors, such as phototransistors, photoresistors, and IR receivers.  
* **Connectors Module**: Handles connectivity via Wi-Fi, Bluetooth, Zigbee, and more.  
* **Transmit Module**: Enables data transmission using MQTT, HTTP, and other protocols.  
* **Modularity**: Add new modules for sensors, communication methods, or transmission protocols without altering the core system.  
* **Custom Sensor Configuration**: Adjust sensitivity using a voltage divider circuit for sensors like phototransistors.

## **How It Works**

### **1\. Data Source Module**

Reads input signals from sensors. For example, the phototransistor circuit uses a voltage divider to adjust sensitivity and convert analogue signals to digital.

### **2\. Connectors Module**

Manages communication with external devices. The system supports adding new protocols such as Bluetooth by simply creating a new module.

### **3\. Transmit Module**

Transmits processed data to external systems or servers. Currently supports MQTT and can be extended to use protocols like HTTP.

## **Example Usage**

The current implementation includes:

1. **Sensor**: Phototransistor setup for reading light intensity.  
2. **Connectivity**: Wi-Fi module for connecting to a local network.  
3. **Transmission**: MQTT protocol to send data to a broker.

### **Code Snippet**

| `# Initialize the sensor, Wi-Fi, and MQTT modules   reader = ReaderSFH300(33)   wifi = WiFiClient('SSID', 'password')   mqtt = MQTT_Client('broker_address', 1883, None, None)   # Connect to Wi-Fi and MQTT   wifi.connect()   mqtt.connect()   # Periodically read data and transmit it   while True:       data = reader.get_counter()       reader.clear_counter()       mqtt.send_topic("gen_electricity_meter/Wh", {"current_consumption": data})       sleep(60)` |
| :---- |

## **Installation**

See the **QUICK START GUIDE.pdf**

## **Prerequisites**

* **MicroPython** installed on ESP32.  
* MQTT broker setup (e.g., Mosquitto).  
* Basic electronics knowledge (Ohm’s Law, voltage divider circuits).

## **Future Improvements**

* Support additional sensors, such as temperature or humidity sensors.  
* Add new communication protocols, like Zigbee or Bluetooth.  
* Extend data transmission options to support protocols like HTTP or WebSocket.