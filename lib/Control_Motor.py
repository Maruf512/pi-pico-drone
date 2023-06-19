import time
from machine import Pin, PWM

class BLDC():
    def __init__(self):
        # Variabls
        self.motor_freq = 27
        self.motor_init_position = 2000
        #self.RPM = 2800 		#H-4900 L-1800

        # output pins
        self.ESC_PIN_1 = Pin(12, Pin.OUT)
        self.ESC_PIN_2 = Pin(13, Pin.OUT)
        self.ESC_PIN_3 = Pin(14, Pin.OUT)
        self.ESC_PIN_4 = Pin(15, Pin.OUT)
        # PWM Object
        self.ESC_1 = PWM(self.ESC_PIN_1)
        self.ESC_2 = PWM(self.ESC_PIN_2)
        self.ESC_3 = PWM(self.ESC_PIN_3)
        self.ESC_4 = PWM(self.ESC_PIN_4)

        # Set the PWM frequency, servo use 50 Hz.
        self.ESC_1.freq(self.motor_freq)		# tested with 30
        self.ESC_2.freq(self.motor_freq)
        self.ESC_3.freq(self.motor_freq)
        self.ESC_4.freq(self.motor_freq)

        self.ESC_1.duty_u16(self.motor_init_position)
        self.ESC_2.duty_u16(self.motor_init_position)
        self.ESC_3.duty_u16(self.motor_init_position)
        self.ESC_4.duty_u16(self.motor_init_position)
        time.sleep(6)

    def BLDC_Duty(self, RPM):
        print(RPM)

        # To output PWM signal to Motors
        self.ESC_1.duty_u16(RPM) 			#H-4900 L-1800
        self.ESC_2.duty_u16(RPM)
        self.ESC_3.duty_u16(RPM)
        self.ESC_4.duty_u16(RPM)
        time.sleep(0.1)



s = BLDC()
while True:
    rpm = input("Enter the RPM: ")
    s.BLDC_Duty(int(rpm))


