
import enum


FRAME_SYNC=0xff

class NodeTypes(enum.Enum):
    TEXT_NODE = 0xa2


class Commands(enum.Enum):
    NONE = 0x0
    MASK = 0x80
    WIDTH = 0xd0
    HEIGHT = 0xd1
    HORIZONTAL_OFFSET = 0xd2
    VERTICAL_OFFSET = 0xd3
    FONT = 0xd4



class Fonts(enum.Enum):
    TEXT_5PX = 0x72  # Large letters only
    TEXT_6PX = 0x66
    TEXT_7PX = 0x65
    TEXT_7PX_BOLD = 0x64
    TEXT_9PX = 0x75
    TEXT_9PX_BOLD = 0x70
    TEXT_9PX_BOLDER = 0x62
    TEXT_13PX = 0x73
    TEXT_13PX_BOLD = 0x69
    TEXT_13PX_BOLDER = 0x61
    TEXT_13PX_BOLDEST = 0x79
    NUMBERS_14PX = 0x00
    TEXT_15PX = 0x71
    TEXT_16PX = 0x68
    TEXT_16PX_BOLD = 0x78
    TEXT_16PX_BOLDER = 0x74
    TEXT_14PX = 0x6f # TODO confirm
    SYMBOLS = 0x67
    PIXEL_BLOCK_5 = 0x77 # Five vertical pixel blocks with bit 0x20..0x3F set


#    PIXELS = 0x20 # ? 5 pixel from

class FrameError(Exception):
    """Exception raised for errors in the frame.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message



def calcChecksum(frame):
    checksum = 0
    for byte in frame:
        checksum += int(byte)
    return checksum & 0xff


