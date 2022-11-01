

import pymobitec_coder

import argparse





def parseFrame(frame):
  if not isFrame(frame):
    raise pymobitec_coder.FrameError("frame check", "not a frame")
  #if not isChecksumGood(frame):
  #  raise FrameError("checksum check", "checksum wrong")
  
  frame = frame[1:-1] # remove FRAME_SYNC
  if frame[-2] == 0xfe:
    checksum_calc = pymobitec_coder.calcChecksum(frame[:-2])
    checksum_frame = frame[-1] + 0xfe
    frame = frame[:-2] # remove checksum
  else:
    checksum_calc = pymobitec_coder.calcChecksum(frame[:-1])
    checksum_frame = frame[-1]
    frame = frame[:-1] # remove checksum
  
  print("Checksum calcualted :", hex(checksum_calc), ", Checksum frame :", hex(checksum_frame))

  address, frame = getAddress(frame)
  print("Address:", address)
  pos = 0
  while pos < len(frame): # TODO checksum
      print("pos:", pos)
      if isCommand(frame, pos):
          pos, command, data = getCommand(frame, pos)
          print(command.name, data, hex(data))
      else:
          while pos < len(frame) and isCommand(frame, pos) is False:
              print(chr(frame[pos]), hex(frame[pos]))
              pos = pos+1
  
  
  return False



""" starts with 0xff and ends with 0xff """
def isFrame(frame):
  if frame[0] == 0xff and frame[-1] == 0xff:
    return True
  return False

def isCommand(frame, pos):
  for command in pymobitec_coder.Commands:
      if frame[pos] == command.value:
          return True
  return False
   

def getCommand(frame, pos):
  for command in pymobitec_coder.Commands:
      if frame[pos] == command.value:
          return pos+2, command, frame[pos+1]
  
def getHeader():
  return False
  
def isChecksumGood(frame, length):
  # calc checksum
  checksum = frame[-1]
  if checksum == 0x00 or checksum == 0x01:
    raise FrameError("checksum", "not parseable")
    
  return False


def getAddress(frame):
   ret = frame[0]
   frame = frame[1:]
   return int(ret), frame



parser = argparse.ArgumentParser()
parser.add_argument("message", help="The mobitec message in hex",
                    type=str)
args = parser.parse_args()

print(args.message)

message = bytearray.fromhex(args.message)

print(message)

parseFrame(message)

# Accept hex string
# print json




