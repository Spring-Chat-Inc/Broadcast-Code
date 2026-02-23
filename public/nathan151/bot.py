from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

from Broadcast import Broadcast


CHANNEL = 151

MOTOR_SETS = [
    [
        Motor(Port.F, Direction.COUNTERCLOCKWISE)
    ], [
        Motor(Port.B)
    ]
]

HAMMER_SPEED = 700
HAMMER_SWING = -135

right1 = Motor(Port.A)
right2 = Motor(Port.D)
left1  = Motor(Port.C, Direction.COUNTERCLOCKWISE)
left2  = Motor(Port.E, Direction.COUNTERCLOCKWISE)

def hammer_swing():
    right1.run_angle(HAMMER_SPEED,  HAMMER_SWING, wait=False)
    right2.run_angle(HAMMER_SPEED,  HAMMER_SWING, wait=False)
    left1.run_angle( HAMMER_SPEED,  HAMMER_SWING, wait=False)
    left2.run_angle( HAMMER_SPEED,  HAMMER_SWING)

    wait(150)

    right1.run_angle(HAMMER_SPEED, -HAMMER_SWING, wait=False)
    right2.run_angle(HAMMER_SPEED, -HAMMER_SWING, wait=False)
    left1.run_angle( HAMMER_SPEED, -HAMMER_SWING, wait=False)
    left2.run_angle( HAMMER_SPEED, -HAMMER_SWING)

def drive_motor_sets(data):
    speed = data[0:2]
    is_hammer = data[2]

    for motor_set_index in range(2):
        for motor in MOTOR_SETS[motor_set_index]:
            # Speed is a percentage (0-100)
            # Max speed: 1000
            motor.run(speed[motor_set_index] * 10)

    if is_hammer:
        hammer_swing()

receiver = Broadcast(callback=drive_motor_sets, observe_channels=[CHANNEL])

receiver.run_receiver()