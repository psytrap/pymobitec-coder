import serial
import time


import argparse



parser = argparse.ArgumentParser()
parser.add_argument("serial_device", help="The name of the serial device",
                    type=str)
args = parser.parse_args()


ser = serial.Serial(args.serial_device, 4800, timeout=0.5)

while True:
    try:
        time.sleep(0.1)
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            data = ser.read(bytesToRead)
            print(data.hex())
   except KeyboardInterrupt:
       print('Program Stopped Manually!')
       ser.close()
       raise

