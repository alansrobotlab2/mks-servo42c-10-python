from mksservo42c_10 import MKSServo42C

servo = MKSServo42C(
    port='/dev/ttyACM0',  # Replace with your serial port
    baudrate=115200,  # Default baudrate for MKSServo42C10 is 9600
    timeout=1,  # Timeout for serial communication
    address=0xE0,  # Default address for MKSServo42C10 ix 0xE0
)

servo.set_subdivision(0x08)

"""
simple example that moves x pulses in the CW direction

with a 1.8 degree servo with subdivisions = 8

(360 degrees / 1.8 degrees) * 8 = 1600 pulses per revolution
so 1600 pulses = 1 revolution

with the pitch and number of teeth you can calculate distance

for example if you have a 20 tooth gear with a pitch of 2.0 mm
then the distance moved is

(20 teeth * 2.0 mm) / 1600 pulses = 0.025 mm per pulse
so if you want to move 1 mm then you need to move 40 pulses
(1 mm / 0.025 mm per pulse) = 40 pulses

"""

servo.move_to("CW",0x70,0x0080)

