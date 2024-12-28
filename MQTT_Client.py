from umqtt.simple import MQTTClient
import uasyncio as asyncio
import json

class MQTT_Client:
    
    def __init__(self, mqtt_broker, mqtt_port, mqtt_user, mqtt_password, client_id="esp32_client"):
        self.__client = MQTTClient(client_id=client_id,
                                   server=mqtt_broker,
                                   port=mqtt_port,
                                   user=mqtt_user,
                                   password=mqtt_password)
        
    def connect(self):
        try:
            self.__client.connect()
            print("Connected to MQTT broker")
        except Exception as e:
            print("Failed to connect to MQTT broker:", e)
    
    def subscribe_to_topic(self, topic):
        try:
            topic_bytes = topic.encode('utf-8')  # Convert topic string to bytes
            self.__client.set_callback(self.__message_handler)
            self.__client.subscribe(topic_bytes)
            print("Subscribed to topic:", topic)
        except Exception as e:
            print("Failed to subscribe to topic:", e)
    
    def disconnect(self):
        try:
            self.__client.disconnect()
            print("Disconnected from MQTT broker")
        except Exception as e:
            print("Failed to disconnect from MQTT broker:", e)
    
    def __message_handler(self, topic, msg):
        print("Received message on topic:", topic)
        print("Message:", msg.decode())
    
    async def wait_for_messages(self):
        try:
            while True:
                await asyncio.sleep_ms(100)
                self.__client.wait_msg()
        except KeyboardInterrupt:
            print("Exiting...")
    
    def send_topic(self, topic:str, data:dict):
        print('Start sending topic')
        try:
            print('trying')
            self.__client.publish(topic, json.dumps(data)) # topic, message
            print("sent")
        except KeyboardInterrupt:
            print("Exiting...")
            return
        except Exception as e:
            print(e)
