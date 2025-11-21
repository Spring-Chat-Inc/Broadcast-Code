from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port

from Broadcast import Broadcast


CHANNEL = 17

INPUT_PAIRS = [
    [
        ForceSensor(Port.A),
        ForceSensor(Port.E)
    ], [
        ForceSensor(Port.B),
        ForceSensor(Port.F)
    ]
]

def send_force_sensor_data():
    data = []
    
    for forward, backward in INPUT_PAIRS:
        # Max force: 10
        force = forward.force() - backward.force()

        percentage = force * 10
        percentage = min(max(100, percentage), 0)

        data.append(percentage)

    return data

sender = Broadcast(broadcast_channel=CHANNEL, callback=send_force_sensor_data)

sender.run_sender()