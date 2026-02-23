from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port

from Broadcast import Broadcast


CHANNEL = 3

COMPONENTS = [
    {
        "name": "Base",
        "port": "A",
        "min": 0,
        "max": 360
    },
    {
        "name": "Secondary Arm",
        "port": "D",
        "min": 204,
        "max": 311
    },{
        "name": "Primary Arm",
        "port": "E",
        "min": 8,
        "max": 149
    },{
        "name": "Gripper",
        "port": "C",
        "min": 136,
        "max": 238
    }
]

MOTORS = [
    Motor(Port.A),
    Motor(Port.D),
    Motor(Port.E),
    Motor(Port.C),
]

def percent_to_degree(min, max, percentage):
    return min + ((max - min) * percentage)

def get_degree(component, percentage, leverage = 5):
    min = component["min"] + leverage
    max = component["max"] - leverage
    
    true_percent = percentage / 100
    
    degree = int(percent_to_degree(min, max, true_percent))
    return degree

def run_motor(motor, degree):
    motor.run_target(100, degree)
    
def main(data):
    for i in range(len(data)):
        component = COMPONENTS[i]
        motor = MOTORS[i]

        percent = data[i]
        degree = get_degree(component, percent)
        run_motor(motor, degree)

#receiver = Broadcast(callback=main, observe_channels=[CHANNEL])

#receiver.run_receiver()

test = [0, 50, 50, 0]
main(test)