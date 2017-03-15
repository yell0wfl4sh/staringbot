import serial
import time
ser=serial.Serial('/dev/ttyUSB0',9600)
i=0
while (i==0):
    ser.write("5")
    time.sleep(0.5)
