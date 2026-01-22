"""
Code for: Jeff
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port

from Broadcast import Broadcast


CHANNEL = 17

INPUT_MOTORS = [
    Motor(Port.A),
    Motor(Port.B, Direction.COUNTERCLOCKWISE)
]

for motor in INPUT_MOTORS:
    motor.reset_angle(0)

def send_force_sensor_data():
    data = []
    
    for motor in INPUT_MOTORS:
        angle = motor.angle()
        angle = max(min(90, angle), -90)

        if angle < 10 and angle > -10:
            angle = 0

        angle = int(angle / 90 * 100)

        data.append(angle)

    return data

sender = Broadcast(callback=send_force_sensor_data, broadcast_channel=CHANNEL)

sender.run_sender()