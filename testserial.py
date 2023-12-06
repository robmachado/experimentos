import serial
import time

ser = serial.Serial(
    "/dev/ttyACM0",
    9600,
    8,
    "N",
    1,
    1
)

i = 0
while i < 10:
    readedText = ser.readline()
    print(readedText)
    i += 1
    time.sleep(0.5)


ser.close()