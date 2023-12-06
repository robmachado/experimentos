import serial
import time


#port = '/dev/ttyUSB0'
#baudrate = 9600
#parity = serial.PARITY_NONE
#stopbits = serial.STOPBITS_ONE
#bytesize = serial.EIGHTBITS

ser = serial(
    port = "/dev/ttyUSB0",
    baudrate = 9600,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS
)

while 1:
    x = ser.readLine()
    print(x)


