# pymobitec-coder
Takes place of a Mobitec Zebra 300 and directly communicating with the Flipdot array.

Requires a RS-485 Dongle as a serial device. Use a Laptop connected with the RS-485 access the Mobitec bus with jumper cables as used by breadboards. Disconnect the Mobitec device and check details about powering the Flipdot array.

Run the utilities to bring up the setup and program the Flipdot array:
* ser_dump.py converts serial data into hex code. It helps to caputure Mobitec Zebra 300 for debugging
* pymobitec-decoder helps to debug encoded data from original Mobitec devices or the encoder utility
* pymobitec-encoder converts a simple JSON format into encoded Mobitec control data.

# Demo
![Demo image of a programmed Flipdot array](../../raw/main/flipdot_demo.jpeg)

