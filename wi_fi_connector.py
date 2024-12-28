import network
import usocket as socket
import ujson
import time

class WiFiClient:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(False)
    
    def connect(self):
        self.sta_if.active(True)
        self.sta_if.connect(self.ssid, self.password)
        for i in range(5):
            if self.sta_if.isconnected():
                print('Connected to WiFi')
                print('IP:', self.sta_if.ifconfig()[0])
                return
            else:
                print('Failed to connect to WiFi')
                time.sleep(1)