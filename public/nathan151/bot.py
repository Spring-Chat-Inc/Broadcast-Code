from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port

from Broadcast import Broadcast


CHANNEL = 151

INPUT_PAIRS = [
    [
        ForceSensor(Port.A),
        ForceSensor(Port.E)
    ], [
        ForceSensor(Port.B),
        ForceSensor(Port.F)
    ]
]

hammer = ForceSensor(Port.D)

def send_force_sensor_data():
    data = []
    
    for forward, backward in INPUT_PAIRS:
        # Max force: 10
        force = forward.force() - backward.force()

        percentage = force * 10
        percentage = max(min(100, percentage), -100)

        data.append(percentage)

    data.append(hammer.pressed())

    return data

sender = Broadcast(callback=send_force_sensor_data, broadcast_channel=CHANNEL)

sender.run_sender()