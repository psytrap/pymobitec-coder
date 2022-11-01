import serial
import time


import argparse



parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument("--hex", help="The mobitec message as hex encode file", type=str)
parser.add_argument("--port", help="Send message to the serial port", type=str)                    
args = parser.parse_args()




ser = serial.Serial(args.port, 4800, timeout=0.5)

if args.hex is not None:
    with open(args.hex, 'r') as hex_file:
        for line in hex_file:
            line = line.rstrip()
            b = bytes.fromhex(line) #.decode("hex") #bytearray(line, "ascii")
            print(b.hex())
            ser.write(b)
            time.sleep(3)
    ser.close()
    exit()



while True:
    try:
        time.sleep(.1)
        bytesToRead = ser.inWaiting()
        if bytesToRead > 0:
            data = ser.read(bytesToRead)
            print(data.hex())
    except KeyboardInterrupt:
       print('Program Stopped Manually!')
       ser.close()
       raise

