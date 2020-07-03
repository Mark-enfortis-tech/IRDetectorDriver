
import time
from serial import Serial

class Ir_serial:
    rx_buffer = []

    def __init__(self, baudrate):
        self.ser = Serial('/dev/ttyAMA0', baudrate=baudrate)

    def isOpen(self):
        return self.ser.isOpen()

    def close(self):
        self.ser.close()

    def read(self):

        try:
            if self.ser.inWaiting() > 0:
                data = self.ser.read()
                print(data)

        except KeyboardInterrupt:
            print('leaving program')

        except:
            print('Error occured, exit reading')



#if __name__ == '__main__':
 #   ser IR_serial(9600)