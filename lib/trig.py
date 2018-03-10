from machine import Pin
import time

class TRIG:
    def __init__(self, pin1, pin2):

        self.result_p10 = None
        self.result_p25 = None
        self.start_p10 = 0
        self.start_p25 = 0

        if pin1 is not None:
            self.pin_p10 = Pin(pin1, Pin.IN, pull = Pin.PULL_UP)
            self.pin_p10.callback(Pin.IRQ_RISING | Pin.IRQ_FALLING, self.trig_p10)

        if pin2 is not None:
            self.pin_p25 = Pin(pin2, Pin.IN, pull = Pin.PULL_UP)
            self.pin_p25.callback(Pin.IRQ_RISING | Pin.IRQ_FALLING, self.trig_p25)

    def trig_p10(self, pin):

        if self.pin_p10.value() == 1:
            self.start_p10 = time.ticks_us()
        elif self.start_p10 is not 0:
            self.result_p10 = time.ticks_diff(self.start_p10, time.ticks_us())
            self.start_p10 = 0

    def trig_p25(self, pin):

        if self.pin_p25.value() == 1:
            self.start_p25 = time.ticks_us()
        elif self.start_p25 is not 0:
            self.result_p25 = time.ticks_diff(self.start_p25, time.ticks_us())
            self.start_p25 = 0

    def getDust_pm10(self):

        if self.result_p10 is None:
            return None
        else:
            result = self.result_p10
            self.result_p10 = None
            return result

    def getDust_pm25(self):

        if self.result_p25 is None:
            return None
        else:
            result = self.result_p25
            self.result_p25 = None
            return result
