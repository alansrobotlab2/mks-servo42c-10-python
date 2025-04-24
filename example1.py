from mksservo42c_10 import MKSServo42C

servo = MKSServo42C(
    port='/dev/ttyACM0',  # Replace with your serial port
    baudrate=115200,  # Default baudrate for MKSServo42C10 is 9600
    timeout=1,  # Timeout for serial communication
    address=0xE0,  # Default address for MKSServo42C10 ix 0xE0
)

print(f"Pulses Recieved: {servo.read_pulses_received()}")
print(f"Motor Shaft Status: {servo.read_motor_shaft_status()}")
print(f"Motor Shaft Angle: {servo.read_motor_shaft_angle()}")
print(f"Motor Shaft Error Angle: {servo.read_motor_shaft_error_angle()}")

