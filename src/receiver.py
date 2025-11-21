from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port

from Broadcast import Broadcast


CHANNEL = 17

MOTOR_SETS = [
    [
        Motor(Port.A)
    ], [
        Motor(Port.D, Direction.COUNTERCLOCKWISE)
    ]
]

def drive_motor_sets(speed):
    for motor_set_index in range(2):
        for motor in MOTOR_SETS[motor_set_index]:
            # Speed is a percentage (0-100)
            # Max speed: 1000
            motor.run(speed[motor_set_index] * 10)

receiver = Broadcast(observe_channels=[CHANNEL], callback=drive_motor_sets)

receiver.run_receiver()