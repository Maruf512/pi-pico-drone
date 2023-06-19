import machine
from machine import Pin, time_pulse_us
import utime

class Recive_Data:
    def __init__(self):
        # CH1 --> GP16, CH2 --> GP18, CH3 --> GP19, CH4 --> GP20, CH5 --> GP21, CH6 --> GP22
        # Initialize PWM receiver pin
        self.all_pins = [Pin(16, Pin.IN), Pin(18, Pin.IN), Pin(19, Pin.IN), Pin(20, Pin.IN), Pin(21, Pin.IN), Pin(22, Pin.IN)]
        self.all_channels_data = []


    # Function to calculate channel value from pulse width
    def calculate_channel_value(self, pulse_width):
        return (pulse_width - 1000) // 10

    def get_data(self):
        #global all_channels_data
        self.all_channels_data.clear()
        
        for pin in self.all_pins:
            print(pin)
            self.pulse_width = self.time_pulse_us(pin, Pin.PULL_DOWN, 30000)			# Read pulse width from PWM receiver pin
            self.data = self.calculate_channel_value(self.pulse_width)					# Calculate channel values
            self.all_channels_data.append(self.pulse_width)


while True:
    rcv_obj = Recive_Data()
    rcv = rcv_obj.get_data()
    print(rcv)
    utime.sleep(0.1)

