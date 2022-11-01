import serial
import serial.tools.list_ports
import pymobitec_coder
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--json", help="The mobitec message as JSON file", type=str)
parser.add_argument("--list", help="List available serial devices", action="store_true")                    
parser.add_argument("--port", help="Send message to the serial port", type=str)                    
args = parser.parse_args()


if args.list is True:
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
    exit()

if args.json is None:
    parser.error('JSON file required')
    exit()

print(args.json)


frame = bytearray()
frame.append(pymobitec_coder.FRAME_SYNC)



# read file
with open(args.json, 'r') as json_file:
    data = json_file.read()
    # parse file
    json = json.loads(data)
    
    #for entry in json:
    #    print(entry, json[entry])
    address = json["address"]
    frame.append(address)
    node_type = pymobitec_coder.NodeTypes[json["node_type"]]
    frame.append(node_type.value)
    payload = json["payload"]
    for entry in payload:
        if isinstance(entry, dict):
            command = pymobitec_coder.Commands[entry["command"]]
            frame.append(command.value)
            if command is pymobitec_coder.Commands.FONT:
                font = pymobitec_coder.Fonts[entry["parameter"]]
                frame.append(font.value)
            else:
                frame.append(entry["parameter"])
        elif isinstance(entry, str):
            print(entry)
            frame.extend(bytearray(entry, "ascii"))

    checksum = pymobitec_coder.calcChecksum(frame[1:])

    print(hex(checksum))
    if checksum == 0xfe:
        frame.append(0xfe)
        frame.append(0x00)
    elif checksum == 0xff:
        frame.append(0xfe)
        frame.append(0x01)
    else:
        frame.append(checksum)
    
    frame.append(pymobitec_coder.FRAME_SYNC)

    print(frame.hex())


if args.port is not None:
    print("Sending message to serial device", args.port)
    ser = serial.Serial(args.port, 4800, timeout=0.5)
    ser.write(frame)


