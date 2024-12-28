from machine import Pin  # Import the Pin module to manage GPIO pins
from abstract_device_connector import AbstractDeviceConnector  # Import an abstract base class for device connectors
from time import ticks_ms, ticks_diff  # Import functions for millisecond timing and calculating time differences

"""
Connection schema:
- VIN to Collector
- Emitter to Pin33 (Value Reader)
- Rin to Emitter
- Rout to GND

This defines how to connect the SFH 300 sensor to the ESP32.
"""

# Define the ReaderSFH300 class, inheriting from AbstractDeviceConnector
class ReaderSFH300(AbstractDeviceConnector):
    
    def __init__(self, pin_number: int):
        """
        Initialize the reader for the SFH300 sensor.
        
        Args:
            pin_number (int): The GPIO pin number where the sensor is connected.
        """
        # Set up the GPIO pin as an input with an interrupt on rising edge
        self.signal_pin = Pin(pin_number, Pin.IN)
        self.signal_pin.irq(trigger=Pin.IRQ_RISING, handler=self.handle_interrupt)
        
        # Initialize internal state variables
        self.signal_state = None  # Tracks the most recent signal state
        self.last_interrupt_time = None  # Tracks the last interrupt time for debouncing
        self.counter = 0  # Tracks the number of valid signal pulses detected
        self.listeners = []  # Placeholder for event listeners (if implemented)

    def handle_interrupt(self, pin):
        """
        Interrupt handler for the sensor. This is triggered on a rising edge of the signal.
        
        Args:
            pin (Pin): The GPIO pin object triggering the interrupt.
        """
        # Get the current time in milliseconds
        current_time = ticks_ms()
        
        # Check if the interrupt is valid (debounce check: at least 30 ms since the last interrupt)
        if self.last_interrupt_time is None or ticks_diff(current_time, self.last_interrupt_time) > 30:
            self.last_interrupt_time = current_time  # Update the last interrupt time
            self.signal_state = pin.value()  # Read the signal state (high/low)
            print(f"Interrupt! Signal: {self.signal_state}, n: {self.counter}")  # Debug message
            self.counter += 1  # Increment the pulse counter

    def get_last_signal(self):
        """
        Retrieve the last recorded signal state.
        
        Returns:
            int: The last signal state (0 or 1).
        """
        return self.signal_state
    
    def get_counter(self):
        """
        Retrieve the current count of pulses detected.
        
        Returns:
            int: The number of pulses since the last reset.
        """
        return self.counter
    
    def clear_counter(self):
        """
        Reset the pulse counter to zero.
        """
        self.counter = 0
