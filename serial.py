import usb.core
import usb.util
import serial
import time

""" comandos do linus
lsusb         - lista os devices usb conectados na maquina
usb-devices   - lista os dados dos devices
dmesg | grep tty - lista as portas tty serial
"""


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


