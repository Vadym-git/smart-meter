"""
    It is an interface for data collectors from the electronic devices
"""


class AbstractDeviceConnector:

    def read_data(self):
        pass
